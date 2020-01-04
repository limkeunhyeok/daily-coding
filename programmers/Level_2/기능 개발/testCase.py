import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([93, 30, 55], [1, 30, 5])
        self.assertEqual(result, [2, 1])
        
if __name__ == '__main__':
    unittest.main()