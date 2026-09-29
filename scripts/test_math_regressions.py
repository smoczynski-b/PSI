#!/usr/bin/env python3
"""Exact counterexamples and witness algebra; these are not general proof checks."""
from fractions import Fraction as F
import unittest


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


class MathWitnessRegression(unittest.TestCase):
    def test_loose_certificate_does_not_equal_condition_number(self):
        # Q=I, A=-I, lambda=1: both certificates satisfy the same hypotheses.
        q = F(1)
        sharp_kappa = q * (1 / q)
        for m, big_m in [(F(1), F(1)), (F(1), F(4)), (F(1, 2), F(9))]:
            self.assertLessEqual(m, q)
            self.assertLessEqual(q, big_m)
            self.assertGreaterEqual(big_m / m, sharp_kappa)
        self.assertNotEqual(F(4) / F(1), sharp_kappa)

    def test_hypocoercive_witness_exact_lyapunov_identity(self):
        a = [[F(0), F(1)], [F(-1), F(-1)]]
        q = [[F(3, 2), F(1, 2)], [F(1, 2), F(1)]]
        aq, qa = mul(transpose(a), q), mul(q, a)
        self.assertEqual([[aq[i][j] + qa[i][j] for j in range(2)] for i in range(2)],
                         [[-1, 0], [0, -1]])
        self.assertEqual(q[0][0] + q[1][1], F(5, 2))
        self.assertEqual(q[0][0] * q[1][1] - q[0][1] * q[1][0], F(5, 4))

    def test_confluence_alone_does_not_give_singleton_image(self):
        # Empty rewrite on two starts: every descendant pair trivially joins.
        descendants = {'a': {'a'}, 'b': {'b'}}
        for reachable in descendants.values():
            for left in reachable:
                for right in reachable:
                    self.assertTrue(descendants[left] & descendants[right])
        normal_forms = {next(iter(reachable)) for reachable in descendants.values()}
        self.assertEqual(len(normal_forms), 2)

    def test_local_alignment_is_not_one_global_rotation(self):
        # Two normal planes with initial angles 0 and 90 degrees. A diagonal
        # gauge preserves their difference; merging deliberately removes it.
        phases = (0, 1)
        for global_rotation in range(4):
            rotated = tuple((phase + global_rotation) % 4 for phase in phases)
            self.assertEqual((rotated[1] - rotated[0]) % 4, 1)
        normalized_phases = (phases[0], phases[0])
        self.assertEqual(normalized_phases[1] - normalized_phases[0], 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
