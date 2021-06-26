import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([2, 7])
        self.assertEqual(result, [3, 11])

if __name__ == '__main__':
    unittest.main()