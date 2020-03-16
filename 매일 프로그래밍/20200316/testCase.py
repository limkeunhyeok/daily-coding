import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 2, 3, 4, 5])
        self.assertEqual(result, [120, 60, 40, 30, 24])
                
    def test_case_2(self):
        result = solution.solution([1, 1, 1, 1, 1])
        self.assertEqual(result, [1, 1, 1, 1, 1])
                
if __name__ == '__main__':
    unittest.main()