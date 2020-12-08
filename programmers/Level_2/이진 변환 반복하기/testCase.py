import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("110010101001")
        self.assertEqual(result, [3, 8])

    def test_case_2(self):
        result = solution.solution("01110")
        self.assertEqual(result, [3, 3])

    def test_case_3(self):
        result = solution.solution("1111111")
        self.assertEqual(result, [4, 1])

if __name__ == '__main__':
    unittest.main()