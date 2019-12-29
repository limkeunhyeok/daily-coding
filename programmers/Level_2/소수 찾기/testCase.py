import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('17')
        self.assertEqual(result, 3)
    
    def test_case_2(self):
        result = solution.solution('011')
        self.assertEqual(result, 2)
if __name__ == '__main__':
    unittest.main()