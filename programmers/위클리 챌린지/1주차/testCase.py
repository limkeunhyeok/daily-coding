import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, 20, 4)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()