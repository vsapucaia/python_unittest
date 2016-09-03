import unittest
from assert_tests.happynumbers import happy_number


class HappynumbersTest(unittest.TestCase):
    def test_number_happy(self):
        for n in (1, 7, 10, 13, 19, 100):
            with self.subTest(n=n):
                self.assertEqual(happy_number(n), True, 'Number %d is not happy.' % n)

    def test_number_not_happy(self):
        for n in (4, 35, 87, 90):
            with self.subTest(n=n):
                self.assertEqual(happy_number(n), False, 'Number %d is happy.' % n)

