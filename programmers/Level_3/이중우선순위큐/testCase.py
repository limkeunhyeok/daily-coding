import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['I 16', 'D 1'])
        self.assertEqual(result, [0, 0])

    def test_case_2(self):
        result = solution.solution(['I 7', 'I 5', 'I -5', 'D -1'])
        self.assertEqual(result, [7, 5])

if __name__ == '__main__':
    unittest.main()