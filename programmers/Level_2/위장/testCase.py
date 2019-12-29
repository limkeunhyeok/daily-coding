import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])
        self.assertEqual(result, 5)

    def test_case_2(self):
        result = solution.solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()