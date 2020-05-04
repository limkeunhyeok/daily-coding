import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[0, 3], [1, 9], [2, 6]])
        self.assertEqual(result, 9)

    def test_case_2(self):
        result = solution.solution([[0, 3], [1, 9], [500, 6]])
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()