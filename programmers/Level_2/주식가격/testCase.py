import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 2, 3, 2, 3])
        self.assertEqual(result, [4, 3, 1, 1, 0])

    def test_case_2(self):
        result = solution.solution([2, 3, 4, 5, 6])
        self.assertEqual(result, [4, 3, 2, 1, 0])

    def test_case_3(self):
        result = solution.solution([2, 3, 4, 5, 4])
        self.assertEqual(result, [4, 3, 2, 1, 0])

    def test_case_4(self):
        result = solution.solution([2, 3, 4, 5, 1])
        self.assertEqual(result, [4, 3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()