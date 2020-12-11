import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("(()())()")
        self.assertEqual(result, "(()())()")
    
    def test_case_2(self):
        result = solution.solution(")(")
        self.assertEqual(result, "()")

    def test_case_3(self):
        result = solution.solution("()))((()")
        self.assertEqual(result, "()(())()")
        
if __name__ == '__main__':
    unittest.main()