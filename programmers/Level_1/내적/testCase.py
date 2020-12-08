import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1,2,3,4], [-3,-1,0,2])
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = solution.solution([-1,0,1], [1,0,-1])
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()