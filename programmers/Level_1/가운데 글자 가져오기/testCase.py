import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('abcde')
        self.assertEqual(result, 'c')
        
    def test_case_2(self):
        result = solution.solution('qwer')
        self.assertEqual(result, 'we')

if __name__ == '__main__':
    unittest.main()