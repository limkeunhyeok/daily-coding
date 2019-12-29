import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('AB', 1)
        self.assertEqual(result, 'BC')
    
    def test_case_2(self):
        result = solution.solution('z', 1)
        self.assertEqual(result, 'a')

    def test_case_3(self):
        result = solution.solution('a B z', 4)
        self.assertEqual(result, 'e F d')

if __name__ == '__main__':
    unittest.main()