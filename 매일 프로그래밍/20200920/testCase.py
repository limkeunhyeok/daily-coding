import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([3, -5, 5, 1, 2, 3])
        self.assertEqual(result, [3, 1, 2, 3])

    def test_case_2(self):
        result = solution.solution([1, 2, 3, 4, -10, 5])
        self.assertEqual(result, [5])

    def test_case_3(self):
        result = solution.solution([10, -3, -4, -3, 1])
        self.assertEqual(result, [1])

    def test_case_4(self):
        result = solution.solution([1, 2, -3 ,3 ,1])
        self.assertEqual(result, [3, 1])

    def test_case_5(self):
        result = solution.solution([1, 2, 3, -3, 4])
        self.assertEqual(result, [1, 2, 4])

    def test_case_6(self):
        result = solution.solution([1, 2, 3, -3, -2])
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()