import unittest
import solution

infos = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

queries = ["java and backend and junior and pizza 100",
           "python and frontend and senior and chicken 200",
           "cpp and - and senior and pizza 250",
           "- and backend and senior and - 150",
           "- and - and - and chicken 100",
           "- and - and - and - 150"]

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(infos, queries)
        self.assertEqual(result, [1, 1, 1, 1, 2, 4])
    
if __name__ == '__main__':
    unittest.main()