import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 2, 3, 7, 10], 7)
        self.assertEqual(result, True)
    
    def test_case_2(self):
        result = solution.solution([-5, -3, 0, 1], 0)
        self.assertEqual(result, True)
    
    def test_case_3(self):
        result = solution.solution([1, 4, 5, 6, 8, 9], 10)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()