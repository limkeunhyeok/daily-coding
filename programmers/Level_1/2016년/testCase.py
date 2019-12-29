import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5, 24)
        self.assertEqual(result, 'TUE')

if __name__ == '__main__':
    unittest.main()