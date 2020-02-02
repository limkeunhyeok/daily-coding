import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5)
        self.assertEqual(result, 26)

    def test_case_2(self):
        result = solution.solution(6)
        self.assertEqual(result, 42)

if __name__ == '__main__':
    unittest.main()