import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
        self.assertEqual(result, "LRLLLRLLRRL")
    
    def test_case_2(self):
        result = solution.solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
        self.assertEqual(result, "LRLLRRLLLRR")

    def test_case_3(self):
        result = solution.solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
        self.assertEqual(result, "LLRLLRLLRL")

if __name__ == '__main__':
    unittest.main()