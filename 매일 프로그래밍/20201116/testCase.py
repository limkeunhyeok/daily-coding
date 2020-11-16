import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([0, 1, 2, 2, 0, 0, 0, 1])
        self.assertEqual(result, [0, 0, 0, 0, 1, 1, 2, 2])

    def test_case_2(self):
        result = solution.solution([0, 1, 2, 0, 1, 2])
        self.assertEqual(result, [0, 0, 1, 1, 2, 2])

    def test_case_3(self):
        result = solution.solution([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
        self.assertEqual(result, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2])

if __name__ == '__main__':
    unittest.main()