import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([120, 110, 140, 150], 485)
        self.assertEqual(result, 127)

if __name__ == '__main__':
    unittest.main()