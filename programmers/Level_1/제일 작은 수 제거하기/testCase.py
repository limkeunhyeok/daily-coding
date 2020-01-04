import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([4, 3, 2, 1])
        self.assertEqual(result, [4, 3, 2])
    
    def test_case_2(self):
        result = solution.solution([10])
        self.assertEqual(result, [-1])

if __name__ == '__main__':
    unittest.main()