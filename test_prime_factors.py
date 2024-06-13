from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_0(self):
        pf = PrimeFactor()
        self.assertEqual(pf.forward(1), [])
        # self.assertEqual(pf.forward(2), [2])

