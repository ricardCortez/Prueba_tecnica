import unittest
from pares_suman_n import pares_suman_n

class TestParesSumanN(unittest.TestCase):
    def test_pares_suman_n(self):
        self.assertEqual(pares_suman_n(10), [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)])

if __name__ == '__main__':
    unittest.main()