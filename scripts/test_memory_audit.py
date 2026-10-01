#!/usr/bin/env python3
"""Adversarial regressions for the implementation audited from conversation 04."""
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import memory_retrieval as memory
from compile_task_contract import compile_task
from compose_task_contract import compile_composed_task, certified_triples
from compile_multilingual_contract import compile_multilingual_task
import resolve_language_fibre as exact
import resolve_uncertain_fibre as uncertain
from relation_crossview import world_crossview, graph_crossview


class MemoryAuditRegression(unittest.TestCase):
    def test_declared_anchor_controls_execution(self):
        for anchor, target in [('II.7', 'II.4'), ('II.9', 'II.7')]:
            contract = compile_task(f'Pokaż przesłanki dowodu {anchor}')
            result = memory.retrieve(contract)
            self.assertEqual(result['anchor'], anchor)
            self.assertIn((anchor, 'HARD_DEPENDS_ON', target), memory.triples(result['edges']))
            if anchor == 'II.7':
                self.assertNotIn('II.9', {e['from'] for e in result['edges']})

    def test_multiple_anchors_do_not_silently_choose_one(self):
        contract = compile_task('Pokaż przesłanki dowodu II.9 i II.7')
        self.assertEqual(contract['status'], 'NEEDS_ANCHOR_POLICY')
        self.assertEqual(memory.retrieve(contract)['edges'], [])

    def test_exclusions_do_not_become_positive_requests(self):
        tasks = [('PL', 'Pomiń zależności dowodowe II.9; pokaż granice.'),
                 ('EN', "Do not retrieve proof prerequisites for II.9; show boundaries."),
                 ('DE', 'II.9 ohne Beweisvoraussetzungen; zeige Grenzen.')]
        for language, task in tasks:
            result = compile_multilingual_task(task, language)
            self.assertEqual(result['stop_condition'], 'NO_RETRIEVAL')
            self.assertEqual(memory.retrieve(result)['edges'], [])
        self.assertEqual(compile_task(tasks[0][1])['stop_condition'], 'NO_RETRIEVAL')
        self.assertEqual(compile_composed_task(tasks[0][1])['stop_condition'], 'NO_RETRIEVAL')

    def test_legitimate_negative_boundary_is_supported(self):
        self.assertEqual(compile_task('dla II.9 pokaż czego twierdzenie nie implikuje')['status'], 'COMPILED')

    def test_strict_evidence_mode_is_executed_without_an_extra_flag(self):
        contract = compile_composed_task('dla II.9 pokaż granice, tylko pełne certyfikaty')
        out = memory.retrieve(contract)
        self.assertEqual(len(out['edges']), 4)
        self.assertTrue(all(e['attestation'] == 'VALID_FRAGMENT_CERT' for e in out['edges']))
        self.assertTrue(out['budget_truncated'])
        complete = memory.retrieve({**contract, 'edge_budget': 10})
        self.assertEqual(len(complete['edges']), 5)
        self.assertFalse(complete['budget_truncated'])

    def test_budget_truncation_is_not_frontier_exhaustion(self):
        contract = compile_task('Pokaż przesłanki dowodu II.9')
        contract['edge_budget'] = 1
        out = memory.retrieve(contract)
        self.assertEqual(len(out['edges']), 1)
        self.assertTrue(out['budget_truncated'])

    def test_bad_runtime_contract_does_not_retrieve(self):
        contract = compile_task('Pokaż przesłanki dowodu II.9')
        for key, value in [('edge_budget', -1), ('edge_budget', True), ('local_radius', float('nan')),
                           ('attestation_mode', 'TRUST_ALL')]:
            bad = {**contract, key: value}
            with self.assertRaises(ValueError):
                memory.retrieve(bad)

    def test_valid_label_does_not_survive_changed_source(self):
        triple = ('II.9', 'NOT_DEPENDS_ON', 'II.8')
        self.assertIn(triple, certified_triples())
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(memory.ROOT / 'docs', root / 'docs')
            source = root / 'docs/principia-v2-09-recursive-history-quotient-update.md'
            # Even a change outside the cited fragment invalidates the frozen blob.
            source.write_text(source.read_text() + '\nSource changed after review.\n')
            with patch.object(memory, 'ROOT', root), patch.object(memory, 'M9', root / 'docs/memory/psi-memory-m9-verified-delta-01.tsv'):
                self.assertNotIn(triple, certified_triples())
                self.assertNotIn(('II.9', 'DOES_NOT_IMPLY', 'BIT-MINIMALITY'), certified_triples())
            # A stale certificate also cannot silently return as a routing hint.
            tables = [root / 'docs/memory' / name for name in (
                'psi-memory-edges-history-01.tsv', 'psi-memory-edges-relational-01.tsv', 'psi-memory-edges-bridges-01.tsv')]
            with patch.object(memory, 'ROOT', root), patch.object(memory, 'M9', root / 'docs/memory/psi-memory-m9-verified-delta-01.tsv'), patch.object(memory, 'TABLES', tables):
                self.assertNotIn(triple, memory.triples(memory.load_attested_edges()))

    def test_fragment_mismatch_rejected(self):
        row = memory.read_tsv(memory.ROOT / 'docs/memory/psi-memory-edge-evidence-01.tsv')[0]
        self.assertTrue(memory.record_is_current(row))
        self.assertFalse(memory.record_is_current({**row, 'fragment_sha256': '0' * 64}))
        self.assertFalse(memory.record_is_current({**row, 'selector': 'absent source fragment'}))

    def test_unknown_relation_is_not_inconsistency(self):
        self.assertEqual(exact.resolve('DE', 'Uhr', [('MAESURES', 'TIME')])['status'], 'NO_RELATION_CONTRACT')
        obs = [{'observation_id': 'x', 'relation': 'MAESURES', 'allowed_values': ['TIME']}]
        out = uncertain.resolve_uncertain('DE', 'Uhr', obs)
        self.assertEqual(out['status'], 'NO_RELATION_CONTRACT')
        self.assertIsNone(out['final_fibre'])
        # A contradiction over a defined relation remains a legitimate empty fibre.
        self.assertEqual(exact.resolve('PL', 'zegarek', [('ATTACHED_TO', 'WALL')])['status'], 'INCONSISTENT')

    def test_tolerance_has_integer_domain(self):
        for invalid in [True, -1, 0.5, float('nan'), float('inf')]:
            with self.assertRaises(ValueError):
                uncertain.resolve_uncertain('DE', 'Uhr', [], invalid)

    def test_observation_values_are_a_set_not_a_string(self):
        with self.assertRaises(ValueError):
            uncertain.resolve_uncertain('DE', 'Uhr', [
                {'observation_id': 'x', 'relation': 'MEASURES', 'allowed_values': 'TIME'}])

    def test_projection_validates_before_empty_selection(self):
        with self.assertRaises(ValueError):
            world_crossview({'TYPO'}, set())
        with self.assertRaises(ValueError):
            graph_crossview({'TYPO'}, set())
        with self.assertRaises(ValueError):
            world_crossview({'MEASURES'}, {'UNKNOWN-ID'})
        self.assertEqual(world_crossview({'MEASURES'}, set())['object_count'], 0)

    def test_identical_material_attributes_do_not_erase_distinct_histories(self):
        # Counterexample suggested by the user's watch example: identities are
        # distinct although the measured material attributes coincide.
        rows = [dict(object_id='A', POSITION='WRIST', MEASURES='TIME', HISTORY='FAMILY'),
                dict(object_id='B', POSITION='WRIST', MEASURES='TIME', HISTORY='SHOP')]
        self.assertEqual(len({(row['POSITION'], row['MEASURES']) for row in rows}), 1)
        self.assertEqual(len({row['HISTORY'] for row in rows}), 2)
        observations = [{'observation_id':'p', 'relation':'POSITION', 'allowed_values':['WRIST']},
                        {'observation_id':'m', 'relation':'MEASURES', 'allowed_values':['TIME']}]
        with patch.object(uncertain, 'world_rows', return_value=rows), patch.object(uncertain, 'lexical_fibre', return_value={'A', 'B'}):
            out = uncertain.resolve_uncertain('PL', 'zegarek', observations)
            self.assertEqual(out['status'], 'UNRESOLVED')
            self.assertEqual(out['final_fibre'], ['A', 'B'])
            observations.append({'observation_id':'h', 'relation':'HISTORY', 'allowed_values':['FAMILY']})
            self.assertEqual(uncertain.resolve_uncertain('PL', 'zegarek', observations)['final_fibre'], ['A'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
