import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 4, 2], [5, 4, 4])
        self.assertEqual(result, 29)
    
    def test_case_2(self):
        result = solution.solution([1, 2], [3, 4])
        self.assertEqual(result, 10)
        
if __name__ == '__main__':
    unittest.main()