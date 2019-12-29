import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([5, 9, 7, 10], 5)
        self.assertEqual(result, [5, 10])
    
    def test_case_2(self):
        result = solution.solution([2, 36, 1, 3], 1)
        self.assertEqual(result, [1, 2, 3, 36])
    
    def test_case_3(self):
        result = solution.solution([3,2,6], 10)
        self.assertEqual(result, [-1])

if __name__ == '__main__':
    unittest.main()