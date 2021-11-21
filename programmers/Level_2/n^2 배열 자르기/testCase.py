import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, 2, 5)
        self.assertEqual(result, [3,2,2,3])

    def test_case_2(self):
        result = solution.solution(4, 7, 14)
        self.assertEqual(result, [4,3,3,3,4,4,4,4])

if __name__ == '__main__':
    unittest.main()