import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(1, 10)
        self.assertEqual(result, [0, 1, 1, 2, 1, 3, 1, 4, 3, 5])

if __name__ == '__main__':
    unittest.main()