import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(8, 12)
        self.assertEqual(result, 80)

if __name__ == '__main__':
    unittest.main()