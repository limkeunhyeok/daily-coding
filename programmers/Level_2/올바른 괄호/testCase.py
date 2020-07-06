import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('()()')
        self.assertEqual(result, True)

    def test_case_2(self):
        result = solution.solution('(())()')
        self.assertEqual(result, True)
    
    
    def test_case_3(self):
        result = solution.solution(')()(')
        self.assertEqual(result, False)
    
    
    def test_case_4(self):
        result = solution.solution('(()(')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()