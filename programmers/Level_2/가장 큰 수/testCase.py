import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([6, 10, 2])
        self.assertEqual(result, '6210')
    
    def test_case_2(self):
        result = solution.solution([3, 30, 34, 5, 9])
        self.assertEqual(result, '9534330')

if __name__ == '__main__':
    unittest.main()