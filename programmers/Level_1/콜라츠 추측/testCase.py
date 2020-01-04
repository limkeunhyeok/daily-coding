import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(6)
        self.assertEqual(result, 8)
    
    def test_case_2(self):
        result = solution.solution(16)
        self.assertEqual(result, 4)

    def test_case_3(self):
        result = solution.solution(626331)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()