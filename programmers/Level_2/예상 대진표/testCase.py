import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(8, 4, 7)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()