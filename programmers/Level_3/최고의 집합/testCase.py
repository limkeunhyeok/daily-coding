import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(2, 9)
        self.assertEqual(result, [4, 5])

    def test_case_2(self):
        result = solution.solution(2, 1)
        self.assertEqual(result, [-1])
        
    def test_case_3(self):
        result = solution.solution(2, 8)
        self.assertEqual(result, [4, 4])

if __name__ == '__main__':
    unittest.main()