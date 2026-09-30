#!/usr/bin/env python3
from __future__ import annotations

import unittest
from unittest.mock import patch

from prepare_memory_evaluation import (bounded_pack, build, make_chunk,
                                       rank_bm25, serialize, source_bytes)


class EvaluationPreparationTests(unittest.TestCase):
    def test_baseline_responds_to_query_without_graph_or_expected_answer(self):
        chunks = [make_chunk('a.md', 1, ['historia historia plansza\n']),
                  make_chunk('b.md', 1, ['metryka operator norma\n'])]
        self.assertEqual(rank_bm25(chunks, 'historia')[0]['path'], 'a.md')
        self.assertEqual(rank_bm25(chunks, 'norma')[0]['path'], 'b.md')
        self.assertEqual(rank_bm25(chunks, 'nieobecne'), [])
        for k1, b in [(True, .75), (float('nan'), .75), (1.2, 2), (1.2, float('inf'))]:
            with self.assertRaises(ValueError):
                rank_bm25(chunks, 'historia', k1, b)

    def test_budget_includes_utf8_and_source_wrappers(self):
        chunks = [make_chunk('żółć.md', 1, ['zażółć gęślą jaźń\n'])]
        cost = len(serialize(chunks).encode())
        self.assertEqual(bounded_pack(chunks, cost), chunks)
        self.assertEqual(bounded_pack(chunks, cost - 1), [])
        self.assertEqual(bounded_pack(chunks, 0), [])
        for invalid in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                bounded_pack(chunks, invalid)

    def test_preparation_is_reproducible_and_has_no_model_success(self):
        first, prompts = build()
        second, again = build()
        self.assertEqual(first, second)
        self.assertEqual(prompts, again)
        self.assertEqual(first['model_status'], 'NOT_RUN')
        self.assertEqual(set(prompts), {'A', 'B', 'C'})
        self.assertLessEqual(first['arms']['C']['context_bytes'], first['arms']['B']['context_bytes'])
        self.assertTrue(first['arms']['C']['chunks'])
        for chunks in [v['chunks'] for v in first['arms'].values()]:
            self.assertTrue(all(len(c['sha256']) == 64 for c in chunks))

    def test_current_uncommitted_source_changes_cannot_change_frozen_inputs(self):
        # Changing local source text must not silently redefine the experiment.
        original = source_bytes('772bd92eb67f314bf99402462e9ec69392abcb5f', 'docs/core.md')
        with patch('pathlib.Path.read_text', side_effect=AssertionError('working-tree source read')):
            self.assertEqual(source_bytes('772bd92eb67f314bf99402462e9ec69392abcb5f', 'docs/core.md'), original)

    def test_gold_protocol_is_never_read_by_preparer(self):
        from prepare_memory_evaluation import source_bytes as real_read
        accessed = []
        def audited(ref, path):
            accessed.append(path)
            return real_read(ref, path)
        with patch('prepare_memory_evaluation.source_bytes', side_effect=audited):
            build()
        self.assertNotIn('experiments/PSI-MEMORY-M4-01.md', accessed)
        self.assertNotIn('experiments/PSI-MEMORY-M4-EVALUATION.md', accessed)
        self.assertTrue(all('RESULT' not in path for path in accessed))


if __name__ == '__main__':
    unittest.main()
