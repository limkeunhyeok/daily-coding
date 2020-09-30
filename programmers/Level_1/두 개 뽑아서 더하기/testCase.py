import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([2,1,3,4,1])
        self.assertEqual(result, [2,3,4,5,6,7])

    def test_case_2(self):
        result = solution.solution([5,0,2,7])
        self.assertEqual(result, [2,5,7,9,12])

if __name__ == '__main__':
    unittest.main()