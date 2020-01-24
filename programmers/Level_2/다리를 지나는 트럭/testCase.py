import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(2, 10, [7,4,5,6])
        self.assertEqual(result, 8)
    
    def test_case_2(self):
        result = solution.solution(100, 100, [10])
        self.assertEqual(result, 101)

    def test_case_3(self):
        result = solution.solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
        self.assertEqual(result, 110)
    
if __name__ == '__main__':
    unittest.main()