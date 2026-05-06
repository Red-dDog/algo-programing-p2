import unittest
import os
import csv
from src.lab7 import find_minimum_cable_length, read_matrix_from_csv

class TestLab7(unittest.TestCase):
    def setUp(self):
        self.test_csv_path = 'test_islands.csv'
        self.test_matrix = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]
        
        with open(self.test_csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(self.test_matrix)

    def tearDown(self):
        if os.path.exists(self.test_csv_path):
            os.remove(self.test_csv_path)

    def test_find_minimum_cable_length_standard(self):
        self.assertEqual(find_minimum_cable_length(self.test_matrix), 16)

    def test_single_island(self):
        self.assertEqual(find_minimum_cable_length([[0]]), 0)

    def test_read_matrix_from_csv(self):
        parsed_matrix = read_matrix_from_csv(self.test_csv_path)
        self.assertEqual(parsed_matrix, self.test_matrix)

    def test_disconnected_graph(self):
        disconnected_matrix = [
            [0, 2, 0],
            [2, 0, 0],
            [0, 0, 0]
        ]
        with self.assertRaises(ValueError):
            find_minimum_cable_length(disconnected_matrix)

if __name__ == '__main__':
    unittest.main()