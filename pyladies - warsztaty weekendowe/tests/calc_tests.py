from unittest import TestCase

from kalkulator import Calc


class CalcTests(TestCase):
    def setUp(self):
        self._calc = Calc()

    def test_add(self):
        self.assertEqual(self._calc.add(3, 4), 7)

    def test_add2(self):
        self.assertEqual(self._calc.add(12, -3), 9)

    def test_mult(self):
        self.assertEqual(self._calc.mult(3, 4), 12)
