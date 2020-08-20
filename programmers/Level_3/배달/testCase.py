import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
        self.assertEqual(result, 4)

    def test_case_2(self):
        result = solution.solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()