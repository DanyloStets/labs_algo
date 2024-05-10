import unittest
from src.gamer_server_ping import *


class TestGameServerLatency(unittest.TestCase):
    def test_incomplete_connections_list(self):
        find_shortest_ping("../test/resoures/game.in", "../test/resoures/game.out")
        with open('../test/resoures/game.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]), 410)

    def test_big_num(self):
        find_shortest_ping("../test/resoures/gamsrv3.in", "../test/resources/gamsrv3.out")
        with open('../test/resources/gamsrv3.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), 1000000050)

if __name__ == '__main__':
    unittest.main()