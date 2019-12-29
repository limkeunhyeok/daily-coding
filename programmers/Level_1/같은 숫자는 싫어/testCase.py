import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1,1,3,3,0,1,1])
        self.assertEqual(result, [1,3,0,1])
    
    def test_case_1(self):
        result = solution.solution([4,4,4,3,3])
        self.assertEqual(result, [4,3])

if __name__ == '__main__':
    unittest.main()