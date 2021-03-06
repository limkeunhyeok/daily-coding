import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
        self.assertEqual(result, 9)

    def test_case_2(self):
        result = solution.solution([[0,0,1,1],[1,1,1,1]])
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()