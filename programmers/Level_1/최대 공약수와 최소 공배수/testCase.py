import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, 12)
        self.assertEqual(result, [3, 12])
    
    def test_case_2(self):
        result = solution.solution(2, 5)
        self.assertEqual(result, [1, 10])

if __name__ == '__main__':
    unittest.main()