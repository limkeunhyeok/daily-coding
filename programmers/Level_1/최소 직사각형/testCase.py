import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[60, 50], [30, 70], [60, 30], [80, 40]])
        self.assertEqual(result, 4000)
    
    def test_case_2(self):
        result = solution.solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
        self.assertEqual(result, 120)

    def test_case_3(self):
        result = solution.solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
        self.assertEqual(result, 133)

if __name__ == '__main__':
    unittest.main()