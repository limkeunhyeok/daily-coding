import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([4, 7, 12], [True, False, True])
        self.assertEqual(result, 9)
    
    def test_case_2(self):
        result = solution.solution([1, 2, 3], [False, False, True])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()