import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([1, 2, 4, 0, 3])
        self.assertEqual(result, True)
                
    def test_case_2(self):
        result = solution.solution([1, 4, 5, 0, 3, 2])
        self.assertEqual(result, False)

    def test_case_3(self):
        result = solution.solution([1, 2, 2, 0])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()