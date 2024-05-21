
import unittest

from src.lab3_algo import BinaryTree,find_bigger

class InorderTest(unittest.TestCase):
    def test_built_in(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.parent = root
        root.right.parent = root

        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)
        root.right.right.parent = root.right
        root.right.right.left.parent = root.right.right

        self.assertEqual(find_bigger(root, root.left.right), 10)
        
    def test_case_2(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.left.parent = root

        root.right = BinaryTree(15)
        root.right.parent = root

        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.left.left.parent = root.left
        root.left.right.parent = root.left

        root.right.right = BinaryTree(20)
        root.right.right.parent = root.right
        root.right.left = BinaryTree(12)
        root.right.left.parent = root.right

        root.right.left.right = BinaryTree(13)
        root.right.left.right.parent = root.right.left
        root.right.left.left = BinaryTree(11)
        root.right.left.left.parent = root.right.left

        root.right.right.right = BinaryTree(23)
        root.right.right.left = BinaryTree(16)
        root.right.right.right.parent = root.right.right
        root.right.right.left.parent = root.right.right
        self.assertEqual(find_bigger(root, root.right.right.left), 20)

if __name__ == '__main__':
    unittest.main()