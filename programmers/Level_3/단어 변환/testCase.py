import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
        self.assertEqual(result, 4)

    def test_case_2(self):
        result = solution.solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()