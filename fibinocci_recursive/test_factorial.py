from unittest import TestCase
from factorial import getFactorial


class TestFactorial(TestCase):

    def test_factorial_numbers(self):
        fact_5 = 120
        fact_1 = 1
        fact_3 = 6
        self.assertEqual(getFactorial(5),fact_5)
        self.assertEqual(getFactorial(1),fact_1)
        self.assertEqual(getFactorial(3),fact_3)


    def test_factorial_zero(self):
        fact_0 = 1
        self.assertEqual(getFactorial(0),fact_0)

    def test_factorial_none(self):
        fact_none = 0
        self.assertEqual(getFactorial(),fact_none)
