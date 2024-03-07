import unittest
import sys
sys.path.append('D:\\PyCharm\\lab2')
from src.lab2_algo import max_hamsters
class TestMaxHamsters(unittest.TestCase):
    def test_lab2_1(self):
        sum_of_eat = 100
        count_of_hamsters = 5
        hamsters = [[10, 5], [20, 3], [15, 2], [25, 4], [30, 1]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 3)

    def test_lab2_2(self):
        sum_of_eat = 5
        count_of_hamsters = 3
        hamsters = [[3, 2], [2, 3], [4, 1]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 1)

    def test_lab2_3(self):
        sum_of_eat = 20
        count_of_hamsters = 4
        hamsters = [[5, 2], [5, 3], [5, 4], [5, 5]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 2)

    def test_lab2_4(self):
        sum_of_eat = 15
        count_of_hamsters = 3
        hamsters = [[5, 2], [5, 2], [5, 2]]
        self.assertEqual(max_hamsters(sum_of_eat, count_of_hamsters, hamsters), 2)
if __name__ == "__main__":
    unittest.main()