import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['Jane', 'Kim'])
        self.assertEqual(result, '김서방은 1에 있다')

if __name__ == '__main__':
    unittest.main()