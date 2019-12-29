import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['leo', 'kiki', 'eden'], ['eden', 'kiki'])
        self.assertEqual(result, 'leo')
    
    def test_case_2(self):
        result = solution.solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola'])
        self.assertEqual(result, 'vinko')

    def test_case_3(self):
        result = solution.solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav'])
        self.assertEqual(result, 'mislav')
if __name__ == '__main__':
    unittest.main()