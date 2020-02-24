import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('abc 123 apple')
        self.assertEqual(result, 'cba 321 elppa')
                
if __name__ == '__main__':
    unittest.main()