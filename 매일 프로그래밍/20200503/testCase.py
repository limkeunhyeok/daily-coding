import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(
            [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]])
        self.assertEqual(result, '1, 2, 3, 4, 5, 6, 7, 8, 9')
                
    def test_case_2(self):
        result = solution.solution(
            [[1, 2, 3, 4],
             [10, 11, 12, 5],
             [9, 8, 7, 6]])
        self.assertEqual(result, '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12')

    def test_case_3(self):
        result = solution.solution(
            [[1, 2, 3, 4, 5, 6],
             [18, 19, 20, 21, 22, 7],
             [17, 28, 29, 30, 23, 8],
             [16, 27, 26, 25, 24, 9],
             [15, 14, 13, 12, 11, 10]])
        self.assertEqual(result, '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30')

if __name__ == '__main__':
    unittest.main()