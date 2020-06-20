import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([[-2,-1], [1,2],[-3,0]])
        self.assertEqual(result, 2)

    def test_case_2(self):
        result = solution.solution([[0,0],])
        self.assertEqual(result, 1)

    def test_case_3(self):
        result = solution.solution([[0,1], [0,1], [1,2]])
        self.assertEqual(result, 1)

    def test_case_4(self):
        result = solution.solution([[0,1], [2,3], [4,5], [6,7]])
        self.assertEqual(result, 4)

    def test_case_5(self):
        result = solution.solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
        self.assertEqual(result, 2)

    def test_case_6(self):
        result = solution.solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
        self.assertEqual(result, 2)

    def test_case_7(self):
        result = solution.solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()