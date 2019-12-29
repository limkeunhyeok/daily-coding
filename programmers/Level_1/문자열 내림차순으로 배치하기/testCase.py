import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('Zbcdefg')
        self.assertEqual(result, 'gfedcbZ')

if __name__ == '__main__':
    unittest.main()