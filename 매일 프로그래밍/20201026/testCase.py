import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([12, 3, 4, 1, 6, 9], 24)
        self.assertEqual(result, [[3, 9, 12]])

    def test_case_2(self):
        result = solution.solution([1, 2, 3, 4, 5], 9)
        self.assertEqual(result, [[1, 3, 5], [2, 3, 4]])

    def test_case_3(self):
        result = solution.solution([1, 4, 45, 6, 10, 8], 22)
        self.assertEqual(result, [[4, 8, 10]])
    
    def test_case_4(self):
        result = solution.solution([1, 2, 3], 6)
        self.assertEqual(result, [[1, 2, 3]])
    
    def test_case_5(self):
        result = solution.solution([1, 2, 3], 5)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()