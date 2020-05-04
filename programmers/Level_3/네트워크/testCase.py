import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
        self.assertEqual(result, 2)

    def test_case_2(self):
        result = solution.solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])
        self.assertEqual(result, 1)
    
    def test_case_3(self):
        result = solution.solution(4, [[1,0,0,1],[0,1,1,1],[0,1,1,0],[1,1,0,1]])
        self.assertEqual(result, 1)
        
if __name__ == '__main__':
    unittest.main()
