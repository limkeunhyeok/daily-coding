import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution1([1, 2, 3, 4, 4])
        self.assertEqual(result, 4)
    
    def test_case_2(self):
        result = solution.solution2([1, 2, 3, 4, 4])
        self.assertEqual(result, 4)

    def test_case_3(self):
        result = solution.solution1([1, 2, 3, 4, 2])
        self.assertEqual(result, 2)
    
    def test_case_4(self):
        result = solution.solution2([1, 2, 3, 4, 2])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()