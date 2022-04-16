import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
        self.assertEqual(result, [2, 1, 1, 0])

    def test_case_2(self):
        result = solution.solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)
        self.assertEqual(result, [0, 0])

if __name__ == '__main__':
    unittest.main()