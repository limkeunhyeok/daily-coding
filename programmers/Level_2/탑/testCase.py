import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([6,9,5,7,4])
        self.assertEqual(result, [0,0,2,2,4])
    
    def test_case_2(self):
        result = solution.solution([3,9,9,3,5,7,2])
        self.assertEqual(result, [0,0,0,3,3,3,6])

    def test_case_3(self):
        result = solution.solution([1,5,3,6,7,6,5])
        self.assertEqual(result, [0,0,2,0,0,5,6])

if __name__ == '__main__':
    unittest.main()