import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([-30, 1, 4, 60])
        self.assertEqual(result, 1)

    def test_case_2(self):
        result = solution.solution([0, 3, 10, 60])
        self.assertEqual(result, 0)

    def test_case_3(self):
        result = solution.solution([-40, -30, -20, 3])
        self.assertEqual(result, 3)

    def test_case_4(self):
        result = solution.solution([-10, -5, 0, 3, 7])
        self.assertEqual(result, 3)

    def test_case_5(self):
        result = solution.solution([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13])
        self.assertEqual(result, 2)

    def test_case_6(self):
        result = solution.solution([-10, -5, 3, 4, 7, 9])
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()