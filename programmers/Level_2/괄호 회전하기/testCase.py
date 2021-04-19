import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("[](){}")
        self.assertEqual(result, 3)
    
    def test_case_2(self):
        result = solution.solution("}]()[{")
        self.assertEqual(result, 2)

    def test_case_3(self):
        result = solution.solution("[)(")
        self.assertEqual(result, 0)

    def test_case_4(self):
        result = solution.solution("}}}")
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()