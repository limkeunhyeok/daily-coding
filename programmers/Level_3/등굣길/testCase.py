import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(4, 3, [[2, 2]])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()