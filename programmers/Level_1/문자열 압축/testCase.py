import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("aabbaccc")
        self.assertEqual(result, 7)
    
    def test_case_2(self):
        result = solution.solution("ababcdcdababcdcd")
        self.assertEqual(result, 9)

    def test_case_3(self):
        result = solution.solution("abcabcdede")
        self.assertEqual(result, 8)
    
    def test_case_4(self):
        result = solution.solution("abcabcabcabcdededededede")
        self.assertEqual(result, 14)
    
    def test_case_5(self):
        result = solution.solution("xababcdcdababcdcd")
        self.assertEqual(result, 17)

if __name__ == '__main__':
    unittest.main()