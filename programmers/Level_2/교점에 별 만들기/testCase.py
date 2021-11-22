import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
        self.assertEqual(result, ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"])
    
    def test_case_2(self):
        result = solution.solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
        self.assertEqual(result, ["*.*"])
    
    def test_case_3(self):
        result = solution.solution([[1, -1, 0], [2, -1, 0]])
        self.assertEqual(result, ["*"])
    
    def test_case_4(self):
        result = solution.solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
        self.assertEqual(result, ["*"])
        
if __name__ == '__main__':
    unittest.main()