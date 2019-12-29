import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(123)
        self.assertEqual(result, 6)
    
    def test_case_2(self):
        result = solution.solution(987)
        self.assertEqual(result, 24)

if __name__ == '__main__':
    unittest.main()