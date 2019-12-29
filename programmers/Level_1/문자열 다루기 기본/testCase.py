import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('a234')
        self.assertEqual(result, False)

    def test_case_2(self):
        result = solution.solution('1234')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()