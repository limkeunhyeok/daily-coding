import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(10)
        self.assertEqual(result, 4)
    
    def test_case_2(self):
        result = solution.solution(5)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()