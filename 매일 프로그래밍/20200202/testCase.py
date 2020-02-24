import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[2, 4], [1, 5], [7, 9]])
        self.assertEqual(result, [[1, 5], [7, 9]])
    
    def test_case_2(self):
        result = solution.solution([[3, 6], [1, 3], [2, 4]])
        self.assertEqual(result, [[1, 6]])
                
if __name__ == '__main__':
    unittest.main()