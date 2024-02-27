import unittest
import sys
sys.path.append('C:\\labsPy\\lab1_algo_Py\\src\\')
from lab1Py.lab1_algo_L3 import zig_zag_in_arr


class TestZigZag(unittest.TestCase):
    def test_zigzag(self):
        zig_arr = [[1,2,3],
                   [4,5,6],
                   [7,8,9]]
        result = zig_zag_in_arr(zig_arr)
        self.assertEqual(result, [1,2,4,7,5,3,6,8,9])
    def test_lab5(self):
        result = zig_zag_in_arr([[1,2],[3,4],[5,6],[7,8]])
        self.assertEqual(result, [1, 2, 3, 5, 4, 6, 7, 8])
    def test_zigzag_lab1(self):
        result = zig_zag_in_arr([[1,2,3,4,5],
                                [6,7,8,9,10],
                                [11,12,13,14,15],
                                [16,17,18,19,20],
                                [21,22,23,24,25]])
        self.assertEqual(result, [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25])
    def test_lab2(self):
        arr = [[1,2],
               [3,4],
               [5,6],
               [7,8]]
        result = zig_zag_in_arr(arr)
        self.assertEqual(result, [1, 2, 3, 5, 4, 6, 7, 8]) 
    def tets_lab4(self):
        result = zig_zag_in_arr([1,2,3,4,5,6])
        self.assertEqual(result, [1,2,3,4,5,6])
    def test_lab3(self):
        result = zig_zag_in_arr([[1]])
        self.assertEqual(result, [1])
        


if __name__ == "__main__":
    unittest.main()