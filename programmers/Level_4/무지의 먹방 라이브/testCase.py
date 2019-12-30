import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([3, 1, 2], 5)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()