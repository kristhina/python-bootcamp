import unittest

from krysia_stats.wektor import Vector


class VectorTests(unittest.TestCase):
    def test_minimum1(self):
        vector = Vector([1, 5, -2, 3])
        self.assertEqual(vector.get_min(), -2)

    def test_maximum1(self):
        vector = Vector([1, 5, -2, 3])
        self.assertEqual(vector.get_max(), 5)

    def test_average1(self):
        vector = Vector([1, 3, 2, 1, 3])
        self.assertEqual(vector.get_average(), 2)

    def test_median1(self):
        vector = Vector([1, 3, 2, 1, 3, 8, -6])
        self.assertEqual(vector.get_median(), 2)

    def test_median2(self):
        vector = Vector([1, 3, 2, 1, 3, 0, -6, 8])
        self.assertEqual(vector.get_median(), 1.5)