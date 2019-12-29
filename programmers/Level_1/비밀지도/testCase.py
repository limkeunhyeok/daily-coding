import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
        self.assertEqual(result, ["#####", "# # #", "### #", "#  ##", "#####"])

    def test_case_2(self):
        result = solution.solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
        self.assertEqual(result, ["######", "###  #", "##  ##", " #### ", " #####", "### # "])

if __name__ == '__main__':
    unittest.main()