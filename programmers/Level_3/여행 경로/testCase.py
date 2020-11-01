import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']])
        self.assertEqual(result, ['ICN', 'JFK', 'HND', 'IAD'])
    
    def test_case_2(self):
        result = solution.solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']])
        self.assertEqual(result, ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])
    
    def test_case_3(self):
        result = solution.solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']])
        self.assertEqual(result, ['ICN', 'B', 'ICN', 'A'])

if __name__ == '__main__':
    unittest.main()