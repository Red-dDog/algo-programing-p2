import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab9 import search_fsa

class TestFSASearch(unittest.TestCase):
    
    def test_basic_search(self):
        haystack = "AABAACAADAABAABA"
        needle = "AABA"
        self.assertEqual(search_fsa(haystack, needle), [0, 9, 12])
        
    def test_no_match(self):
        haystack = "HELLO WORLD"
        needle = "XYZ"
        self.assertEqual(search_fsa(haystack, needle), [])
        
    def test_empty_needle(self):
        self.assertEqual(search_fsa("HELLO", ""), [])
        
    def test_empty_haystack(self):
        self.assertEqual(search_fsa("", "HELLO"), [])
        
    def test_overlapping_matches(self):
        self.assertEqual(search_fsa("AAAAA", "AA"), [0, 1, 2, 3])
        
    def test_needle_larger_than_haystack(self):
        self.assertEqual(search_fsa("A", "AA"), [])
        
    def test_full_match(self):
        self.assertEqual(search_fsa("EXACTMATCH", "EXACTMATCH"), [0])
        
    def test_special_characters(self):
        self.assertEqual(search_fsa("a!b!c! a!b!", "a!b!"), [0, 7])

if __name__ == '__main__':
    unittest.main()