import unittest
import test

class temp(unittest.TestCase):
    def test_case_1(self):
        result = test.solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA'])
        self.assertEqual(result, 50)
    
    def test_case_2(self):
        result = test.solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul'])
        self.assertEqual(result, 21)
if __name__ == '__main__':
    unittest.main()