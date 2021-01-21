import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([8, 7, 2, 5, 3, 1], 10)
        self.assertEqual(result, [[8, 2], [7, 3]])

if __name__ == '__main__':
    unittest.main()