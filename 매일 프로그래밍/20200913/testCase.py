import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 2, 3, 4, 6, 7, 8, 9, 10])
        self.assertEqual(result, 5)

    def test_case_2(self):
        result = solution.solution([1, 2, 4, 5, 6])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()