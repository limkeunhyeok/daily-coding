import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([10, 5, 4, 3, -1])
        self.assertEqual(result, 5)

    def test_case_2(self):
        result = solution.solution([3, 3, 3])
        self.assertEqual(result, 'Does not exist.')
                
if __name__ == '__main__':
    unittest.main()