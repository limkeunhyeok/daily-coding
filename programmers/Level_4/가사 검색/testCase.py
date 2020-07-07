import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
        self.assertEqual(result, [3, 2, 4, 1, 0])

if __name__ == '__main__':
    unittest.main()