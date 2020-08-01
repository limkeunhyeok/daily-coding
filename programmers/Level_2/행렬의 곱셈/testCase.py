import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
        self.assertEqual(result, [[15, 15], [15, 15], [15, 15]])
    
    def test_case_2(self):
        result = solution.solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
        self.assertEqual(result, [[22, 22, 11], [36, 28, 18], [29, 20, 14]])
                
if __name__ == '__main__':
    unittest.main()