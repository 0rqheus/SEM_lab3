import unittest
import sys

sys.path.append('../lab3')
from get_file_stats import get_file_stats

class TestStats(unittest.TestCase):
    def test_add(self):
        stats = get_file_stats('./tests/example.py.txt')
        self.assertEqual(stats['physical_lines'], 36)
        self.assertEqual(stats['code_lines'], 27)
        self.assertEqual(stats['logical_lines'], 9)
        self.assertEqual(stats['empty_lines'], 8)
        self.assertEqual(stats['comment_lines'], 3)
        self.assertEqual(stats['comment_level'], 4)

if __name__ == "__main__":
    unittest.main()