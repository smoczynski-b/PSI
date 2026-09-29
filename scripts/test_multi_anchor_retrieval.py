#!/usr/bin/env python3
from __future__ import annotations

import unittest

import memory_retrieval as memory
from multi_anchor_retrieval import (
    canonical_signature,
    compile_multi_anchor_task,
    execute_multi_anchor,
)


class MultiAnchorRetrievalRegression(unittest.TestCase):
    def test_two_anchors_without_operator_fail_closed(self):
        contract = compile_multi_anchor_task('sprawdź przesłanki dowodu II.9 i II.7')
        self.assertEqual(contract['status'], 'NEEDS_ANCHOR_POLICY')
        self.assertEqual(contract['stop_condition'], 'NO_RETRIEVAL')
        self.assertEqual(execute_multi_anchor(contract)['status'], 'NO_RETRIEVAL')

    def test_compare_is_symmetric_up_to_anchor_labels(self):
        left = compile_multi_anchor_task('porównaj przesłanki dowodu II.9 i II.7')
        right = compile_multi_anchor_task('porównaj przesłanki dowodu II.7 i II.9')
        self.assertEqual(left['status'], 'COMPILED')
        self.assertEqual(right['status'], 'COMPILED')
        out_left = execute_multi_anchor(left)
        out_right = execute_multi_anchor(right)
        self.assertEqual(canonical_signature(out_left), canonical_signature(out_right))
        self.assertIn(('II.9', 'HARD_DEPENDS_ON', 'II.7'), memory.triples(out_left['cross_edges']))
        self.assertEqual(out_left['budget_mode'], 'EQUAL_PER_ANCHOR')

    def test_intersection_is_commutative_and_subset_of_both_views(self):
        c1 = compile_multi_anchor_task('pokaż wspólne przesłanki dowodu II.9 i II.7')
        c2 = compile_multi_anchor_task('pokaż wspólne przesłanki dowodu II.7 i II.9')
        out1 = execute_multi_anchor(c1)
        out2 = execute_multi_anchor(c2)
        self.assertEqual(canonical_signature(out1), canonical_signature(out2))
        common = memory.triples(out1['common_edges'])
        self.assertTrue(common)
        for view in out1['views'].values():
            self.assertTrue(common <= memory.triples(view['edges']))

    def test_intersection_does_not_invent_edges(self):
        contract = compile_multi_anchor_task('pokaż wspólne przesłanki dowodu II.9 i II.7')
        out = execute_multi_anchor(contract)
        left, right = contract['anchors']
        expected = memory.triples(out['views'][left]['edges']) & memory.triples(out['views'][right]['edges'])
        self.assertEqual(memory.triples(out['common_edges']), expected)

    def test_transfer_is_directional_and_does_not_invert_dependency(self):
        forward = compile_multi_anchor_task('przenieś kontekst przesłanek dowodu z II.9 do II.7')
        backward = compile_multi_anchor_task('przenieś kontekst przesłanek dowodu z II.7 do II.9')
        out_forward = execute_multi_anchor(forward)
        out_backward = execute_multi_anchor(backward)
        self.assertEqual(out_forward['status'], 'RETRIEVED')
        self.assertEqual((out_forward['source'], out_forward['target']), ('II.9', 'II.7'))
        self.assertEqual(memory.triples(out_forward['route']), {('II.9', 'HARD_DEPENDS_ON', 'II.7')})
        self.assertEqual(out_forward['transferred_view']['anchor'], 'II.7')
        self.assertEqual(out_backward['status'], 'NO_ROUTE')
        self.assertIsNone(out_backward['transferred_view'])

    def test_strict_evidence_mode_propagates_to_each_operand_and_route(self):
        compare = compile_multi_anchor_task('porównaj przesłanki dowodu II.9 i II.7, tylko pełne certyfikaty')
        out = execute_multi_anchor(compare)
        self.assertEqual(compare['attestation_mode'], 'VALID_FRAGMENT_CERT_ONLY')
        for view in out['views'].values():
            self.assertTrue(view['edges'])
            self.assertTrue(all(e['attestation'] == 'VALID_FRAGMENT_CERT' for e in view['edges']))
        self.assertTrue(all(e['attestation'] == 'VALID_FRAGMENT_CERT' for e in out['cross_edges']))

        transfer = compile_multi_anchor_task('przenieś kontekst przesłanek dowodu z II.9 do II.7, tylko pełne certyfikaty')
        moved = execute_multi_anchor(transfer)
        self.assertEqual(moved['status'], 'RETRIEVED')
        self.assertTrue(all(e['attestation'] == 'VALID_FRAGMENT_CERT' for e in moved['route']))
        self.assertTrue(all(e['attestation'] == 'VALID_FRAGMENT_CERT' for e in moved['transferred_view']['edges']))

    def test_operators_are_not_aliases_for_one_merged_neighbourhood(self):
        compare = execute_multi_anchor(compile_multi_anchor_task('porównaj przesłanki dowodu II.9 i II.7'))
        intersect = execute_multi_anchor(compile_multi_anchor_task('pokaż wspólne przesłanki dowodu II.9 i II.7'))
        transfer = execute_multi_anchor(compile_multi_anchor_task('przenieś kontekst przesłanek dowodu z II.9 do II.7'))
        self.assertIn('views', compare)
        self.assertIn('common_edges', intersect)
        self.assertIn('route', transfer)
        self.assertNotEqual(compare['operator'], intersect['operator'])
        self.assertNotEqual(intersect['operator'], transfer['operator'])

    def test_invalid_multi_anchor_budget_is_rejected(self):
        contract = compile_multi_anchor_task('porównaj przesłanki dowodu II.9 i II.7')
        for key, value in [('per_anchor_edge_budget', -1), ('per_anchor_edge_budget', True), ('route_budget', 0)]:
            bad = {**contract, key: value}
            with self.assertRaises(ValueError):
                execute_multi_anchor(bad)


if __name__ == '__main__':
    unittest.main(verbosity=2)
