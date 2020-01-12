import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([3,1,2,3])
        self.assertEqual(result, 2)

    def test_case_2(self):
        result = solution.solution([3,3,3,2,2,4])
        self.assertEqual(result, 3)
    
    def test_case_3(self):
        result = solution.solution([3,3,3,2,2,2])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()