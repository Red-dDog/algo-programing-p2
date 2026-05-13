import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab8 import count_paths, solve_file

class TestIJones(unittest.TestCase):

    def test_example_1(self):
        w, h = 3, 3
        grid = [
            "aaa",
            "cab",
            "def"
        ]
        self.assertEqual(count_paths(w, h, grid), 5)

    def test_example_2(self):
        w, h = 10, 1
        grid = [
            "abcdefaghi"
        ]
        self.assertEqual(count_paths(w, h, grid), 2)

    def test_example_3(self):
        w, h = 7, 6
        grid = [
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa",
            "aaaaaaa"
        ]
        self.assertEqual(count_paths(w, h, grid), 201684)

    def test_minimal_grid(self):
        w, h = 1, 1
        grid = ["a"]
        self.assertEqual(count_paths(w, h, grid), 1)

    def test_column_grid(self):
        w, h = 1, 3
        grid = ["a", "b", "c"]
        self.assertEqual(count_paths(w, h, grid), 2)

    def test_file_io(self):
        input_file = "test_ijones.in"
        output_file = "test_ijones.out"
        
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write("3 3\naaa\ncab\ndef\n")
            
        solve_file(input_file, output_file)
        
        with open(output_file, 'r', encoding='utf-8') as f:
            res = f.read().strip()
            
        self.assertEqual(res, "5")
        
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)


if __name__ == '__main__':
    unittest.main()