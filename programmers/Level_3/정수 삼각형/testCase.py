import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
        self.assertEqual(result, 30)

if __name__ == '__main__':
    unittest.main()