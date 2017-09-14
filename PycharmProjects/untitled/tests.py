import unittest
from piontec_meczy_zone import is_prime
from piontec_meczy_zone import is_prime_for_list
from average_class import ListStats


class TestPrimes(unittest.TestCase):
    def test_is_prime_12(self):
        self.assertFalse(is_prime(12))

    def test_are_primes(self):
        primes = [3, 5, 7, 11]
        for prime in primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))

    def test_are_primes_for_list(self):
        primes = [2, 3, 4, 5]
        self.assertEqual(is_prime_for_list(primes), [True, True, False, True])


class TestAverage(unittest.TestCase):
    def test_average_123(self):
        numbers_to_average = ListStats([1, 2, 3])
        self.assertEqual(numbers_to_average.get_list_average(), 2)

    def test_average_0(self):
        numbers_to_average = ListStats([-1, 0, 1])
        self.assertEqual(numbers_to_average.get_list_average(), 0)

    def test_average_emptylist(self):
        numbers_to_average = ListStats([])
        with self.assertRaises(Exception):
            numbers_to_average.get_list_average()

    def test_max(self):
        numbers = ListStats([-1, 0, 1])
        self.assertEqual(numbers.get_max(), 1)

    def test_max1(self):
        numbers = ListStats([-1, 0, 1, 5, 3, -4])
        self.assertEqual(numbers.get_max(), 5)

    def test_min(self):
        numbers = ListStats([-1, 0, 1])
        self.assertEqual(numbers.get_min(), -1)

    def test_min1(self):
        numbers = ListStats([-1, 0, 1, 5, -7, 3, -4])
        self.assertEqual(numbers.get_min(), -7)

    def test_median(self):
