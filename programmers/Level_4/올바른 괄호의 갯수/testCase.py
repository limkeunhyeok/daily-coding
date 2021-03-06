import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(1)
        self.assertEqual(result, 1)
    
    def test_case_2(self):
        result = solution.solution(2)
        self.assertEqual(result, 2)

    def test_case_3(self):
        result = solution.solution(3)
        self.assertEqual(result, 5)

    def test_case_4(self):
        result = solution.solution(4)
        self.assertEqual(result, 14)

    def test_case_5(self):
        result = solution.solution(5)
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()