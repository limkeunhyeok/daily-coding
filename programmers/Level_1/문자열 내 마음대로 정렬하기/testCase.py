import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['sun', 'bed', 'car'], 1)
        self.assertEqual(result, ['car', 'bed', 'sun'])
    
    def test_case_2(self):
        result = solution.solution(['abce', 'abcd', 'cdx'], 2)
        self.assertEqual(result, ['abcd', 'abce', 'cdx'])

if __name__ == '__main__':
    unittest.main()