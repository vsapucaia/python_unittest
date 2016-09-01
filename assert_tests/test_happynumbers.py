import unittest
from assert_tests.happynumbers import happy_number


class HappynumbersTest(unittest.TestCase):
    def test_number_happy(self):
        for n in (1, 7, 10, 13, 19, 100):
            self.assertEqual(happy_number(n), True)

    def test_number_not_happy(self):
        for n in (4, 35, 87, 90):
            self.assertEqual(happy_number(n), False)
