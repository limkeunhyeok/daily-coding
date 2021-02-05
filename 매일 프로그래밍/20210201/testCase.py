import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([4, 2, -3, -1, 0, 4])
        self.assertEqual(result, [[0], [-3, -1, 0, 4]])
    
    def test_case_2(self):
        result = solution.solution([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
        self.assertEqual(result,[[3, 4, -7], [4, -7, 3], [3, 1, -4], [-7, 3, 1, 3], [3, 1, 3, 1, -4, -2, -2], [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]])

if __name__ == '__main__':
    unittest.main()