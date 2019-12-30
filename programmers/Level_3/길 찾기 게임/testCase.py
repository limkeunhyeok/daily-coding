import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
        self.assertEqual(result, [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]])

if __name__ == '__main__':
    unittest.main()