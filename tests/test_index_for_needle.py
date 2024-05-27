import unittest
from src.find_index_for_neadle import *

class TestPatternSearch(unittest.TestCase):
    def test_find_occurrences_simple(self):
        pattern = "adada"
        text = "adaddacadadadadaddd"
        expected = [7, 9, 11]
        self.assertEqual(find_needle_indices(text, pattern), expected)

    def test_find_occurrences_no_occurrence(self):
        pattern = "g"
        text = "jfjfjfjfjfjfjfj"
        expected = []
        self.assertEqual(find_needle_indices(text, pattern), expected)