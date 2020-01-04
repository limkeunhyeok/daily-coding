import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(12345)
        self.assertEqual(result, [5,4,3,2,1])

if __name__ == '__main__':
    unittest.main()