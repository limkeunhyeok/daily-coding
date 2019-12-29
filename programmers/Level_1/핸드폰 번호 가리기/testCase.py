import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('01033334444')
        self.assertEqual(result, '*******4444')
    
    def test_case_2(self):
        result = solution.solution('027778888')
        self.assertEqual(result, '*****8888')

if __name__ == '__main__':
    unittest.main()