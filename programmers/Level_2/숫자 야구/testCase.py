import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()