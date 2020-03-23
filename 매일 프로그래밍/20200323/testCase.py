import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([-1, 3, -1, 5, 4], 2)
        self.assertEqual(result, 4)
                
    def test_case_2(self):
        result = solution.solution([2, 4, -2, -3, 8], 1)
        self.assertEqual(result, 8)
    
    def test_case_3(self):
        result = solution.solution([-5, -3, 1], 3)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()