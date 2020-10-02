import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(4, [4, 3, 3])
        self.assertEqual(result, 12)

    def test_case_2(self):
        result = solution.solution(1, [2, 1, 2])
        self.assertEqual(result, 6)

    def test_case_3(self):
        result = solution.solution(3, [1, 1])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()