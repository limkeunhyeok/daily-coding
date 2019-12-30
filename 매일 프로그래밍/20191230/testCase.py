import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([-1, 3, -1, 5])
        self.assertEqual(result, 7)

    def test_case_2(self):
        result = solution.solution([-5, -3, -1])
        self.assertEqual(result, -1)

    def test_case_3(self):
        result = solution.solution([2, 4, -2, -3, 8])
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()