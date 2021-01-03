import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
        self.assertEqual(result, 2)
    
    def test_case_2(self):
        result = solution.solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
        self.assertEqual(result, 2)

    def test_case_3(self):
        result = solution.solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()