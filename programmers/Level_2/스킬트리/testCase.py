import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
        self.assertEqual(result, 2)
    
if __name__ == '__main__':
    unittest.main()