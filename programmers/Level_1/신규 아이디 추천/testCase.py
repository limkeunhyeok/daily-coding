import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("...!@BaT#*..y.abcdefghijklm")
        self.assertEqual(result, "bat.y.abcdefghi")
    
    def test_case_2(self):
        result = solution.solution("z-+.^.")
        self.assertEqual(result, "z--")

    def test_case_3(self):
        result = solution.solution("=.=")
        self.assertEqual(result, "aaa")
    
    def test_case_4(self):
        result = solution.solution("123_.def")
        self.assertEqual(result, "123_.def")

    def test_case_5(self):
        result = solution.solution("abcdefghijklmn.p")
        self.assertEqual(result, "abcdefghijklmn")
    
if __name__ == '__main__':
    unittest.main()
