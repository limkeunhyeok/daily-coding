import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, 5)
        self.assertEqual(result, 12)
    
    def test_case_2(self):
        result = solution.solution(3, 3)
        self.assertEqual(result, 3)
    
    def test_case_3(self):
        result = solution.solution(5, 3)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()