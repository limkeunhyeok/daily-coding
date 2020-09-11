import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("aaabbc")
        self.assertEqual(result, "ababac")
    
    def test_case_2(self):
        result = solution.solution("aaac")
        self.assertEqual(result, "")
    
    def test_case_3(self):
        result = solution.solution("aaabc")
        self.assertEqual(result, "abaca")
    
    def test_case_4(self):
        result = solution.solution("aaabb")
        self.assertEqual(result, "ababa")
    
    def test_case_5(self):
        result = solution.solution("aa")
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()