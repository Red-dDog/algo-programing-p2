import unittest

from lab2 import hamster_calc

class TestHamsters(unittest.TestCase):
    
    def test_example_1(self):
        S, C = 7, 3
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(hamster_calc(S, C, hamsters), 2)

    def test_example_2(self):
        S, C = 19, 4
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(hamster_calc(S, C, hamsters), 3)

    def test_example_3(self):
        S, C = 2, 2
        hamsters = [[1, 50000], [1, 60000]]
        self.assertEqual(hamster_calc(S, C, hamsters), 1)

    def test_example_4(self):
        S, C = 32, 3
        hamsters = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(hamster_calc(S, C, hamsters), 3)

if __name__ == '__main__':
    unittest.main()