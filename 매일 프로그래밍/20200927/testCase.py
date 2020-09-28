import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3)
        self.assertEqual(result, '21')

    def test_case_2(self):
        result = solution.solution(4)
        self.assertEqual(result, '1211')

    def test_case_3(self):
        result = solution.solution(5)
        self.assertEqual(result, '111221')

    def test_case_4(self):
        result = solution.solution(6)
        self.assertEqual(result, '312211')

if __name__ == '__main__':
    unittest.main()