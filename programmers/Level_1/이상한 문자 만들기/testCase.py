import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('try hello world')
        self.assertEqual(result, 'TrY HeLlO WoRlD')

if __name__ == '__main__':
    unittest.main()