import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])
        self.assertEqual(result, [4, 1, 3, 0])

    def test_case_2(self):
        result = solution.solution(['classic', 'classic', 'classic', 'classic', 'pop'], [100, 100, 100, 100, 1000])
        self.assertEqual(result, [4, 0, 1])

if __name__ == '__main__':
    unittest.main()