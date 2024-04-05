import unittest
from src.flood_fill import flood_fill

class TestFloodFill(unittest.TestCase):
    def test_fill_all_field(self):
        with open('resources\\index_all_fill.txt', 
                  'r', 
                  encoding='utf-8'):
            flood_fill('resources\\index_all_fill.txt', 'resources\\index_test_all_fill.txt')
        
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

        

if __name__ == "__main__":
    unittest.main()