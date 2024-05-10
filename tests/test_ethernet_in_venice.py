import unittest
from src.ethernet_in_venice import *

class TestGameServerLatency(unittest.TestCase):
    def test_ethernet_lengh(self):
        find_shortest_lengh_ethernet('resoures/island.csv', 'resoures/island.out')
        with open('resoures/island.out', 'r') as file:
            result = file.readline()
        self.assertEqual(result, '5')

    def test_empty_file(self):
        find_shortest_lengh_ethernet('resoures/island_empty.csv', 'resoures/island_empty.out')
        with open('resoures/island_empty.out', 'r') as file:
            result = file.readline()
        self.assertEqual(result, '')

if __name__ == '__main__':
    unittest.main()