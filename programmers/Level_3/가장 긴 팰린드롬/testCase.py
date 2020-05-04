import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('abcdcba')
        self.assertEqual(result, 7)

    def test_case_2(self):
        result = solution.solution('abacde')
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()