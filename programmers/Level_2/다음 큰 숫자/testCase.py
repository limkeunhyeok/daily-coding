import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(78)
        self.assertEqual(result, 83)

    def test_case_2(self):
        result = solution.solution(15)
        self.assertEqual(result, 23)

if __name__ == '__main__':
    unittest.main()