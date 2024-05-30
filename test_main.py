# test_main.py

import unittest
from main import plus, minus

class TestMain(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(plus(2, 3), 5)
        self.assertEqual(plus(-1, 1), 0)
        self.assertEqual(plus(-1, -1), -2)

    def test_minus(self):
        self.assertEqual(minus(5, 3), 2)
        self.assertEqual(minus(-1, 1), -2)
        self.assertEqual(minus(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
