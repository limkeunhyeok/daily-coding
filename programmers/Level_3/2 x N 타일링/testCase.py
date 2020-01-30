import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(4)
        self.assertEqual(result, 5)

    def test_case_2(self):
        result = solution.solution(3)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()