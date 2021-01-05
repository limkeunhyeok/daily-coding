import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([5, 6, -5, 5, 3, 5, 3, -2, 0], 8)
        self.assertEqual(result, [-5, 5, 3, 5])

if __name__ == '__main__':
    unittest.main()