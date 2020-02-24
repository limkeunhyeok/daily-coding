import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([0, 5, 0, 3, -1])
        self.assertEqual(result, [5, 3, -1, 0, 0])

    def test_case_2(self):
        result = solution.solution([3, 0, 3])
        self.assertEqual(result, [3, 3, 0])
                
if __name__ == '__main__':
    unittest.main()