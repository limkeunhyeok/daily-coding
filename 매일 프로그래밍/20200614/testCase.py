import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([3, 4, 5, 1, 2], 4)
        self.assertEqual(result, 1)
    
    def test_case_2(self):
        result = solution.solution([2, 4, 5, 1], 3)
        self.assertEqual(result, -1)
    
    def test_case_3(self):
        result = solution.solution([4, 6, 7, 8, 1, 2, 3], 5)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()