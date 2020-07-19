import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
        self.assertEqual(result, [3, 7])
    
    def test_case_2(self):
        result = solution.solution(["AA", "AB", "AC", "AA", "AC"])
        self.assertEqual(result, [1, 3])

    def test_case_3(self):
        result = solution.solution(["XYZ", "XYZ", "XYZ"])
        self.assertEqual(result, [1, 1])
    
    def test_case_4(self):
        result = solution.solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
        self.assertEqual(result, [1, 5])

if __name__ == '__main__':
    unittest.main()