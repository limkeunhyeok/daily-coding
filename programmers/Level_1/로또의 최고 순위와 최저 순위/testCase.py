import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
        self.assertEqual(result, [3, 5])
    
    def test_case_2(self):
        result = solution.solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
        self.assertEqual(result, [1, 6])

    def test_case_3(self):
        result = solution.solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
        self.assertEqual(result, [1, 1])

if __name__ == '__main__':
    unittest.main()