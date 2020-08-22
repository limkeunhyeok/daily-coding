import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
        self.assertEqual(result, 3)
        
if __name__ == '__main__':
    unittest.main()