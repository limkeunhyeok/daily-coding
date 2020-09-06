import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([3, 2, 1])
        self.assertEqual(result, 1)
    
    def test_case_2(self):
        result = solution.solution([2, 4, 6, 8])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()