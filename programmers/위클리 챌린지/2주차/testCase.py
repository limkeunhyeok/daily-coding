import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
        self.assertEqual(result, "FBABD")
    
    def test_case_2(self):
        result = solution.solution([[50,90],[50,87]])
        self.assertEqual(result, "DA")
    
    def test_case_3(self):
        result = solution.solution([[70,49,90],[68,50,38],[73,31,100]])
        self.assertEqual(result, "CFD")

if __name__ == '__main__':
    unittest.main()