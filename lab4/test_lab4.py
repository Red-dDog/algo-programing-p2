import unittest

from lab4 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):
    
    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_extract_max(self):
        self.pq.insert("Task 1", 1)
        self.pq.insert("Task 5", 5)
        self.pq.insert("Task 3", 3)
        self.pq.insert("Task 10", 10)
        self.pq.insert("Task 4", 4)

        self.assertEqual(self.pq.extract_max(), ("Task 10", 10))
        self.assertEqual(self.pq.extract_max(), ("Task 5", 5))
        self.assertEqual(self.pq.extract_max(), ("Task 4", 4))
        self.assertEqual(self.pq.extract_max(), ("Task 3", 3))
        self.assertEqual(self.pq.extract_max(), ("Task 1", 1))
        self.assertIsNone(self.pq.extract_max())

    def test_peek(self):
        self.assertIsNone(self.pq.peek())
        
        self.pq.insert("Low Priority", 10)
        self.pq.insert("High Priority", 100)
        self.assertEqual(self.pq.peek(), ("High Priority", 100))
        self.assertEqual(self.pq.extract_max(), ("High Priority", 100))
        self.assertEqual(self.pq.peek(), ("Low Priority", 10))

    def test_empty_queue(self):
        """Перевірка поведінки порожньої черги."""
        self.assertIsNone(self.pq.extract_max())
        self.assertIsNone(self.pq.peek())

    def test_equal_priorities(self):
        """Перевірка роботи з однаковими пріоритетами."""
        self.pq.insert("Task A", 5)
        self.pq.insert("Task B", 5)
        self.pq.insert("Task C", 5)
        
        extracted = []
        for _ in range(3):
            extracted.append(self.pq.extract_max())
            
        self.assertEqual(len(extracted), 3)
        for task in extracted:
            self.assertEqual(task[1], 5)
            self.assertIn(task[0], ["Task A", "Task B", "Task C"])
            
        self.assertIsNone(self.pq.extract_max())

if __name__ == "__main__":
    unittest.main()