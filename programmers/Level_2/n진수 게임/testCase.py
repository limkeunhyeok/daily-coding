import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(2, 4, 2, 1)
        self.assertEqual(result, '0111')

    def test_case_2(self):
        result = solution.solution(16, 16, 2, 1)
        self.assertEqual(result, '02468ACE11111111')

    def test_case_3(self):
        result = solution.solution(16, 16, 2, 2)
        self.assertEqual(result, '13579BDF01234567')

if __name__ == '__main__':
    unittest.main()