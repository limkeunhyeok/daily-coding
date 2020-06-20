import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([2, 1, 3, 2], 2)
        self.assertEqual(result, 1)
    
    def test_case_2(self):
        result = solution.solution([1, 1, 9, 1, 1, 1], 0)
        self.assertEqual(result, 5)

    def test_case_3(self):
        result = solution.solution([3,3,4,2], 3)
        self.assertEqual(result, 4)

    def test_case_4(self):
        result = solution.solution([2,2,2,1,3,4], 3)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()