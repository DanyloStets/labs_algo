import unittest
from src.red_black_priority_queue import RedBlackTree

class TestRedBlackPriorityQueue(unittest.TestCase):
    def test_peek_sequence(self):
        tree = RedBlackTree()
        tree.insert(1, 11)
        tree.insert(30, 10)
        tree.insert(11, 6)
        tree.insert(12, 7)
        tree.insert(13, 3)
        tree.insert(14, 1)
        tree.insert(15, 8)
        tree.insert(16, 4)
        self.assertEqual(tree.delete(11), None)

if __name__ == "__main__":
    unittest.main()