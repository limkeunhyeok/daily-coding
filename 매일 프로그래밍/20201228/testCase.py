import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([2, 0, 2, 1, 4, 3, 1, 0])
        self.assertEqual(result, [0, 2, 1, 4, 3])

if __name__ == '__main__':
    unittest.main()