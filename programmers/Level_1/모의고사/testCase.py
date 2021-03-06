import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1,2,3,4,5])
        self.assertEqual(result, [1])
    
    def test_case_2(self):
        result = solution.solution([1,3,2,4,2])
        self.assertEqual(result, [1,2,3])

if __name__ == '__main__':
    unittest.main()