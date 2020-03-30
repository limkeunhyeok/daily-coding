import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['apple', 'apps', 'ape'])
        self.assertEqual(result, 2)
                
    def test_case_2(self):
        result = solution.solution(['hawaii', 'happy'])
        self.assertEqual(result, 2)
    
    def test_case_3(self):
        result = solution.solution(['dog', 'dogs', 'doge'])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()