import unittest
from src.ethernet_in_venice import *

class TestGameServerLatency(unittest.TestCase):
    def test_ethernet_lengh(self):
        find_shortest_lengh_ethernet('resources/island.csv', 'resources/island.out')
        with open('resources/island.out', 'r') as file:
            result = file.readline()
        self.assertEqual(result, '5')

    def test_empty_file(self):
        find_shortest_lengh_ethernet('resources/island_empty.csv', 'resources/island_empty.out')
        with open('resources/island_empty.out', 'r') as file:
            result = file.readline()
        self.assertEqual(result, '0')

if __name__ == '__main__':
    unittest.main()