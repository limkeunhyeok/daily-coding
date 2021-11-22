import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("AAAAE")
        self.assertEqual(result, 6)
        
    def test_case_2(self):
        result = solution.solution("AAAE")
        self.assertEqual(result, 10)
    
    def test_case_3(self):
        result = solution.solution("I")
        self.assertEqual(result, 1563)
    
    def test_case_4(self):
        result = solution.solution("EIO")
        self.assertEqual(result, 1189)
    
if __name__ == '__main__':
    unittest.main()