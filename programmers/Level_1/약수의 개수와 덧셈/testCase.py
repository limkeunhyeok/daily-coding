import unittest
import solution

class Temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(13, 17)
        self.assertEqual(result, 43)

    def test_case_2(self):
        result = solution.solution(24, 27)
        self.assertEqual(result, 52)

if __name__ == '__main__':
    unittest.main()