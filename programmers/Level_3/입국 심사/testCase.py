import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(6, [7, 10])
        self.assertEqual(result, 28)

if __name__ == '__main__':
    unittest.main()