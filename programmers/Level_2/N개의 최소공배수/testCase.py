import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([2, 6, 8, 14])
        self.assertEqual(result, 168)
    
    def test_case_2(self):
        result = solution.solution([1, 2, 3])
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()