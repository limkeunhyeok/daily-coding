import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['119', '97674223', '1195524421'])
        self.assertEqual(result, False)
    
    def test_case_2(self):
        result = solution.solution(['123', '456', '789'])
        self.assertEqual(result, True)

    def test_case_3(self):
        result = solution.solution(['12', '123', '1235', '567', '88'])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()