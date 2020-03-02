import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('aabcbcbc')
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = solution.solution('aaaaaaaa')
        self.assertEqual(result, 1)
    
    def test_case_3(self):
        result = solution.solution('abbbcedd')
        self.assertEqual(result, 4)
                
if __name__ == '__main__':
    unittest.main()