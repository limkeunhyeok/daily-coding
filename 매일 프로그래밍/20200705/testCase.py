import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 2, 3, 8])
        self.assertEqual(result, 7)
    
    def test_case_2(self):
        result = solution.solution([1, 3, 4, 5])
        self.assertEqual(result, 2)

    def test_case_3(self):
        result = solution.solution([1, 2, 6, 10, 11, 15])
        self.assertEqual(result, 4)

    def test_case_4(self):
        result = solution.solution([1, 1, 1, 1])
        self.assertEqual(result, 5)

    def test_case_5(self):
        result = solution.solution([1, 1, 3, 4])
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()