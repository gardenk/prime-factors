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

    def test_prime_factor_3(self):
        self.assertEqual(self.pf.forward(3), [3])

    def test_prime_factor_4(self):
        self.assertEqual(self.pf.forward(4), [2,2])

    def test_prime_factor_6(self):
        self.assertEqual(self.pf.forward(6), [2,3])