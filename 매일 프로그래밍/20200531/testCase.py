import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution1([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [3, 4, 5, 1, 2])
    
    def test_case_2(self):
        result = solution.solution1([0, 1, 2, 3, 4], 1)
        self.assertEqual(result, [1, 2, 3, 4, 0])
    
    def test_case_3(self):
        result = solution.solution1([25, 7, 11, 14, 24, 5, 17, 35, 8, 36], 4)
        self.assertEqual(result, [24, 5, 17, 35, 8, 36, 25, 7, 11, 14])

    def test_case_4(self):
        result = solution.solution2([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, [3, 4, 5, 1, 2])
    
    def test_case_5(self):
        result = solution.solution2([0, 1, 2, 3, 4], 1)
        self.assertEqual(result, [1, 2, 3, 4, 0])
    
    def test_case_6(self):
        result = solution.solution2([25, 7, 11, 14, 24, 5, 17, 35, 8, 36], 4)
        self.assertEqual(result, [24, 5, 17, 35, 8, 36, 25, 7, 11, 14])

if __name__ == '__main__':
    unittest.main()