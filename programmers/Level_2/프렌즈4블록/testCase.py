import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'])
        self.assertEqual(result, 14)
    
    def test_case_2(self):
        result = solution.solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ'])
        self.assertEqual(result, 15)
    
    def test_case_3(self):
        result = solution.solution(3, 3, ['CCB', 'CCC', 'BCC'])
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()