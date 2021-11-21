import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(80, [[80,20],[50,40],[30,10]])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()