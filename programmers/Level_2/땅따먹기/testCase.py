import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])
        self.assertEqual(result, 16)
    
    def test_case_2(self):
        result = solution.solution([[3, 5, 6, 8], [3, 5, 3, 4], [5, 10, 4, 3], [1, 3000, 2, 1]])
        self.assertEqual(result, 3018)

    def test_case_3(self):
        result = solution.solution([[1, 2, 3, 5], [5, 6, 7, 100], [4, 3, 2, 1]])
        self.assertEqual(result, 107)
        
if __name__ == '__main__':
    unittest.main()