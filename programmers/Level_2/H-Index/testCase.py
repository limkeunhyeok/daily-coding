import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([3, 0, 6, 1, 5])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()