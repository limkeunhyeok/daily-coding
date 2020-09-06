import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("/usr/bin/../")
        self.assertEqual(result, "/usr/")
    
    def test_case_2(self):
        result = solution.solution("/usr/./bin/./test/../")
        self.assertEqual(result, "/usr/bin/")

if __name__ == '__main__':
    unittest.main()