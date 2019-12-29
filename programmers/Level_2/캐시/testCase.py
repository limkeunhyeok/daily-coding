import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])
        self.assertEqual(result, 50)

    def test_case_2(self):
        result = solution.solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'])
        self.assertEqual(result, 21)

    def test_case_3(self):
        result = solution.solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'])
        self.assertEqual(result, 60)

    def test_case_4(self):
        result = solution.solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome'])
        self.assertEqual(result, 52)

    def test_case_5(self):
        result = solution.solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork'])
        self.assertEqual(result, 16)

    def test_case_6(self):
        result = solution.solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()