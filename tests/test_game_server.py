import unittest
from src.gamer_server_ping import *


class TestGameServerLatency(unittest.TestCase):
    def test_incomplete_connections_list(self):
        find_shortest_ping("resources/game.in", "resources/game.out")
        with open('resources/game.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()

        self.assertEqual(int(numbers[0]), 410)

    def test_big_num(self):
        find_shortest_ping("resources/game_exp_2.in", "resources/game_exp_2.out")
        with open('resources/game_exp_2.out', 'r') as file:
            first_line = file.readline()
            numbers = first_line.split()
        self.assertEqual(int(numbers[0]), 1000000050)

if __name__ == '__main__':
    unittest.main()