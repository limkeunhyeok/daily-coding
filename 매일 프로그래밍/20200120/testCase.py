import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(12345)
        self.assertEqual(result, False)
    
    def test_case_2(self):
        result = solution.solution(-101)
        self.assertEqual(result, False)
    
    def test_case_3(self):
        result = solution.solution(11111)
        self.assertEqual(result, True)

    def test_case_4(self):
        result = solution.solution(12421)
        self.assertEqual(result, True)
                
if __name__ == '__main__':
    unittest.main()