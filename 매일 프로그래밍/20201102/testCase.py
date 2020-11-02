import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5)
        self.assertEqual(result, ['00000', '00001', '00010', '00100', '00101', '01000', '01001', '01010', '10000', '10001', '10010', '10100', '10101'])

    def test_case_2(self):
        result = solution.solution(3)
        self.assertEqual(result, ['000', '001', '010', '100', '101'])

if __name__ == '__main__':
    unittest.main()