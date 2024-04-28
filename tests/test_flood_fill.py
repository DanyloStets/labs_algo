import unittest
import sys
sys.path.insert(0, '../src')
from  flood_fill import *
# from src.flood_fill import flood_fill_recolor

class TestFloodFill(unittest.TestCase):
    def test_fill_all_field(self):
        with open('test\\resourcesindex_all_fill.txt', 
                  'r', 
                  encoding='utf-8') as file:
            flood_fill_recolor('tests\\resources\\index_all_fill.txt', 'resources\\index_test_all_fill.txt')
        
        with open('resources\\index_test_all_fill.txt',
                   'r',
                    encoding='utf-8') as file:
            matrix_line1 = file.readline().strip()
            matrix_line2 = file.readline().strip()
            matrix_line3 = file.readline().strip()
            matrix_line4 = file.readline().strip()
            matrix_line5 = file.readline().strip()
            self.assertEqual(matrix_line1,"['R', 'R', 'R', 'R', 'R']")
            self.assertEqual(matrix_line2,"['R', 'R', 'R', 'R', 'R']")
            self.assertEqual(matrix_line3,"['R', 'R', 'R', 'R', 'R']")
            self.assertEqual(matrix_line4,"['R', 'R', 'R', 'R', 'R']")
            self.assertEqual(matrix_line5,"['R', 'R', 'R', 'R', 'R']")

    def test_is_pos_currunt_colour(self):
        with open('resources\\index_pos_is_cur_colour.txt', 
                  'r', 
                  encoding='utf-8'):
            flood_fill_recolor('resources\\index_pos_is_cur_colour', 'resources\\index_test_pos_in_cur_colour.txt')
        with open('resources\\index_test_pos_in_cur_colour.txt',
                   'r',
                    encoding='utf-8') as file:
            matrix_line1 = file.readline().strip()
            matrix_line2 = file.readline().strip()
            matrix_line3 = file.readline().strip()
            matrix_line4 = file.readline().strip()
            self.assertEqual(matrix_line1,"['W', 'W', 'G', 'R', 'R', 'R']")
            self.assertEqual(matrix_line2,"['Y', 'Y', 'G', 'R', 'W', 'R']")
            self.assertEqual(matrix_line3,"['W', 'Y', 'B', 'R', 'Y', 'Y']")
            self.assertEqual(matrix_line4,"['W', 'B', 'B', 'R', 'B', 'B']")

if __name__ == "__main__":
    unittest.main()