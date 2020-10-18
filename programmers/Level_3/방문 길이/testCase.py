import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('ULURRDLLU')
        self.assertEqual(result, 7)

    def test_case_2(self):
        result = solution.solution('LULLLLLLU')
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()