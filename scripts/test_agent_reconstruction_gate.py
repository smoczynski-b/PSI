#!/usr/bin/env python3
"""Regression tests for PSI conversation reconstruction provenance and context isolation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / 'docs/agent-reconstruction-gate-01.md'
AGENTS = ROOT / 'AGENTS.md'

DIRECT = 'DIRECT'
USER = 'USER'
REPO = 'REPO'
MEMORY = 'MEMORY'
INFERRED = 'INFERRED'


def may_claim_read(source_class):
    return source_class == DIRECT


def has_binding_witness(memory_ids, target_ids):
    return bool(set(memory_ids) & set(target_ids))


def may_select_inherited_next(memory_ids, target_ids):
    return has_binding_witness(memory_ids, target_ids)


class ReconstructionGateRegression(unittest.TestCase):
    def test_gate_document_is_bound_from_agents(self):
        self.assertTrue(GATE.is_file())
        agents = AGENTS.read_text(encoding='utf-8')
        self.assertIn('docs/agent-reconstruction-gate-01.md', agents)

    def test_memory_is_not_direct_read(self):
        self.assertFalse(may_claim_read(MEMORY))
        self.assertFalse(may_claim_read(INFERRED))
        self.assertFalse(may_claim_read(REPO))
        self.assertFalse(may_claim_read(USER))
        self.assertTrue(may_claim_read(DIRECT))

    def test_unbound_global_memory_cannot_select_next(self):
        target = {'historical-map', 'sentence-audit', 'source-edition'}
        unrelated = {'operator-theory', 'P9', 'resolvent'}
        self.assertFalse(may_select_inherited_next(unrelated, target))

    def test_bound_state_can_select_next(self):
        target = {'historical-map', 'sentence-audit', 'source-edition'}
        recovered = {'historical-map', 'candidate-pairs', 'source-edition'}
        self.assertTrue(may_select_inherited_next(recovered, target))

    def test_required_invariants_are_documented(self):
        text = GATE.read_text(encoding='utf-8')
        for marker in (
            r'\mathrm{MEMORY}\neq\mathrm{DIRECT}',
            'RECONSTRUCTION-PROVENANCE-LOSS',
            'CROSS-THREAD-CONTAMINATION',
            'FRONTIER SELECT` is illegal before `BIND THREAD` passes',
            'no thread binding',
        ):
            self.assertIn(marker, text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
