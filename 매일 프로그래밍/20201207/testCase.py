import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([0, 6, 3, 4, 0])
        self.assertEqual(result, [0])

    def test_case_2(self):
        result = solution.solution([5, 4, 3, 2, 1, 1, 1, 1, 1, 2])
        self.assertEqual(result, [1, 2])

if __name__ == '__main__':
    unittest.main()