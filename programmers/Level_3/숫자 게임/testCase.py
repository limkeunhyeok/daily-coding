import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([5, 1, 3, 7], [2, 2, 6, 8])
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = solution.solution([2, 2, 2, 2], [1, 1, 1, 1])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()