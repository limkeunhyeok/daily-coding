import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('JEROEN')
        self.assertEqual(result, 56)

    def test_case_2(self):
        result = solution.solution('JAN')
        self.assertEqual(result, 23)

if __name__ == '__main__':
    unittest.main()