import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5, [2, 4], [1, 3, 5])
        self.assertEqual(result, 5)

    def test_case_2(self):
        result = solution.solution(5, [2, 4], [3])
        self.assertEqual(result, 4)

    def test_case_3(self):
        result = solution.solution(3, [3], [1])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()