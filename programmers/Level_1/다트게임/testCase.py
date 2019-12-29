import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('1S2D*3T')
        self.assertEqual(result, 37)

    def test_case_2(self):
        result = solution.solution('1D2S#10S')
        self.assertEqual(result, 9)
    
    def test_case_3(self):
        result = solution.solution('1D2S0T')
        self.assertEqual(result, 3)
    
    def test_case_4(self):
        result = solution.solution('1S*2T*3S')
        self.assertEqual(result, 23)
    
    def test_case_5(self):
        result = solution.solution('1D#2S*3S')
        self.assertEqual(result, 5)
    
    def test_case_6(self):
        result = solution.solution('1T2D3D#')
        self.assertEqual(result, -4)
    
    def test_case_7(self):
        result = solution.solution('1D2S3T*')
        self.assertEqual(result, 59)

if __name__ == '__main__':
    unittest.main()