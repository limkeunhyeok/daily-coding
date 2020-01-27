import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([2, 5, 6, 1, 10], 8)
        self.assertEqual(result, [0, 2])
    
    def test_case_2(self):
        result = solution.solution([2, 5, 6, 1, 10], 7)
        self.assertEqual(result, [0, 1])
    
    def test_case_3(self):
        result = solution.solution([1, 5, 16, 7, 10], 100)
        self.assertEqual(result, -1)

    def test_case_4(self):
        result = solution.solution([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11], 21)
        self.assertEqual(result, [0, 22])
                
if __name__ == '__main__':
    unittest.main()