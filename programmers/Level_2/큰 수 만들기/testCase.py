import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('1924', 2)
        self.assertEqual(result, '94')
    
    def test_case_2(self):
        result = solution.solution('1231234', 3)
        self.assertEqual(result, '3234')
    
    def test_case_3(self):
        result = solution.solution('4177252841', 4)
        self.assertEqual(result, '775841')
         
if __name__ == '__main__':
    unittest.main()