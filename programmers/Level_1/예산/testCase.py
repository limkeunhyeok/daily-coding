import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1,3,2,5,4], 9)
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = solution.solution([2,2,3,3], 10)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()