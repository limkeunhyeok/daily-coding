import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(11, [4, 11], 1)
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = solution.solution(16, [9], 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()