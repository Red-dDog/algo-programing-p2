import unittest
import os
import tempfile
from src.gamsrv import find_optimal_server_latency, solve


class TestGamsrv(unittest.TestCase):
    
    def test_example_1(self):
        """Тестування першого прикладу з умови задачі."""
        num_nodes = 6
        clients = {1, 2, 6}
        edges = [
            (1, 3, 10),
            (3, 4, 80),
            (4, 5, 50),
            (5, 6, 20),
            (2, 3, 40),
            (2, 4, 100)
        ]
        expected = 100
        result = find_optimal_server_latency(num_nodes, clients, edges)
        self.assertEqual(result, expected)

    def test_example_2(self):
        """Тестування другого прикладу з умови задачі (кільцева топологія)."""
        num_nodes = 9
        clients = {2, 4, 6}
        edges = [
            (1, 2, 20), (2, 3, 20), (3, 6, 20), (6, 9, 20),
            (9, 8, 20), (8, 7, 20), (7, 4, 20), (4, 1, 20),
            (5, 2, 10), (5, 4, 10), (5, 6, 10), (5, 8, 10)
        ]
        expected = 10
        result = find_optimal_server_latency(num_nodes, clients, edges)
        self.assertEqual(result, expected)

    def test_example_3(self):
        """Тестування третього прикладу з умови задачі (великі затримки)."""
        num_nodes = 3
        clients = {1, 3}
        edges = [
            (1, 2, 50),
            (2, 3, 1000000000)
        ]
        expected = 1000000000
        result = find_optimal_server_latency(num_nodes, clients, edges)
        self.assertEqual(result, expected)

    def test_solve_file_io(self):
        """Тестування повної функції solve() з читанням/записом файлів."""
        input_data = (
            "6 6\n"
            "1 2 6\n"
            "1 3 10\n"
            "3 4 80\n"
            "4 5 50\n"
            "5 6 20\n"
            "2 3 40\n"
            "2 4 100\n"
        )
        
        # Створюємо тимчасовий вхідний файл
        with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as infile:
            infile.write(input_data)
            in_path = infile.name
            
        out_path = in_path + ".out"
        
        try:
            solve(in_path, out_path)
            with open(out_path, "r", encoding="utf-8") as outfile:
                result = outfile.read().strip()
            self.assertEqual(result, "100")
        finally:
            if os.path.exists(in_path):
                os.remove(in_path)
            if os.path.exists(out_path):
                os.remove(out_path)


if __name__ == '__main__':
    unittest.main()