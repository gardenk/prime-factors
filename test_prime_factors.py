from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_1(self):
        pf = PrimeFactor()
        self.assertEqual(pf.forward(1), [])

    def test_prime_factor_2(self):
        pf = PrimeFactor()
        self.assertEqual(pf.forward(2), [2])

