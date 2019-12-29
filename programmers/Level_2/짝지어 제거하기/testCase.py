import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('baabaa')
        self.assertEqual(result, 1)

    def test_case_2(self):
        result = solution.solution('cdcd')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()