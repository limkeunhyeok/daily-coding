import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])
        self.assertEqual(result, 4)
    
    def test_case_2(self):
        result = solution.solution(4, [[0,1,1],[0,2,2],[2,3,1]])
        self.assertEqual(result, 4)

    def test_case_3(self):
        result = solution.solution(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])
        self.assertEqual(result, 11)

    def test_case_4(self):
        result = solution.solution(4, [[0, 1 ,1], [0, 2, 100], [0, 3, 100], [1, 2, 100], [1, 3, 100], [2, 3, 1]])
        self.assertEqual(result, 102)

if __name__ == '__main__':
    unittest.main()