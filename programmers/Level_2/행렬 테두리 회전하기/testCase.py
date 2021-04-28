import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
        self.assertEqual(result, [8, 10, 25])
    
    def test_case_2(self):
        result = solution.solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
        self.assertEqual(result, [1, 1, 5, 3])

    def test_case_3(self):
        result = solution.solution(100, 97, [[1, 1, 100, 97]])
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()