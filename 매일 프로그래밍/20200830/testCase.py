import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(4)
        self.assertEqual(result, True)

    def test_case_2(self):
        result = solution.solution(16)
        self.assertEqual(result, True)

    def test_case_3(self):
        result = solution.solution(17)
        self.assertEqual(result, False)

    def test_case_4(self):
        result = solution.solution(64)
        self.assertEqual(result, True)

    def test_case_5(self):
        result = solution.solution(256)
        self.assertEqual(result, True)

    def test_case_6(self):
        result = solution.solution(257)
        self.assertEqual(result, False)
    
    def test_case_7(self):
        result = solution.solution(1024)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()