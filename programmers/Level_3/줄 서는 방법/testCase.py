import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, 5)
        self.assertEqual(result, [3, 1, 2])

    def test_case_2(self):
        result = solution.solution(4, 5)
        self.assertEqual(result, [1, 4, 2, 3])

if __name__ == '__main__':
    unittest.main()