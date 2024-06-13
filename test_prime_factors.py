from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self):
        super().setUp()
        self.pf = PrimeFactor()

    def test_prime_factor_1(self):
        self.assertEqual(self.pf.forward(1), [])

    def test_prime_factor_2(self):
        self.assertEqual(self.pf.forward(2), [2])

