import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(118372)
        self.assertEqual(result, 873211)

if __name__ == '__main__':
    unittest.main()