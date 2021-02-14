import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
        self.assertEqual(result, ["AC", "ACDE", "BCFG", "CDE"])
    
    def test_case_2(self):
        result = solution.solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
        self.assertEqual(result, ["ACD", "AD", "ADE", "CD", "XYZ"])

    def test_case_3(self):
        result = solution.solution(["XYZ", "XWY", "WXA"], [2,3,4])
        self.assertEqual(result, ["WX", "XY"])

if __name__ == '__main__':
    unittest.main()