import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 1, 1, 1, 1], 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()