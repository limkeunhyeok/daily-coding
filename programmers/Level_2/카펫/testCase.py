import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(10, 2)
        self.assertEqual(result, [4, 3])
    
    def test_case_2(self):
        result = solution.solution(8, 1)
        self.assertEqual(result, [3, 3])
    
    def test_case_3(self):
        result = solution.solution(24, 24)
        self.assertEqual(result, [8, 6])

if __name__ == '__main__':
    unittest.main()