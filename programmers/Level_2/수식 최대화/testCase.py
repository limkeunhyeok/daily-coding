import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("100-200*300-500+20")
        self.assertEqual(result, 60420)
    
    def test_case_2(self):
        result = solution.solution("50*6-3*2")
        self.assertEqual(result, 300)

if __name__ == '__main__':
    unittest.main()