import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
        self.assertEqual(result, [3,4,2,1,5])

    def test_case_2(self):
        result = solution.solution(4, [4,4,4,4,4])
        self.assertEqual(result, [4, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()