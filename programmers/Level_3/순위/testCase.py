import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()