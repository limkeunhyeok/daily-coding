import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([9,-1,-5])
        self.assertEqual(result, 3)

    def test_case_2(self):
        result = solution.solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()