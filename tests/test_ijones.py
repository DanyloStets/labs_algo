import unittest
from src.Indiana_jones import *


class TestIndianaJones(unittest.TestCase):

    def traversal_IJ_example_1(self):
        len_matrix_row, len_matrix_col, main_matrix = read_input_matrix("resources/ijones_example_1.in")
        result = count_ways(len_matrix_row, len_matrix_col, main_matrix)
        out_put = read_output("resources/ijones_example_1.out")
        self.assertEqual(result, out_put)

    def traversal_IJ_example_2(self):
        len_matrix_row, len_matrix_col, main_matrix = read_input_matrix("resources/ijones_example_2.in")
        result = count_ways(len_matrix_row, len_matrix_col, main_matrix)
        out_put = read_output("resources/ijones_example_2.out")
        self.assertEqual(result, out_put)


if __name__ == '__main__':
    unittest.main()
