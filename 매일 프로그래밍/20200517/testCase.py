import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.quick_sort([1, 2, 4, 0, 3])
        self.assertEqual(result, [0, 1, 2, 3, 4])
    
    def test_case_2(self):
        result = solution.merge_sort([1, 2, 4, 0, 3])
        self.assertEqual(result, [0, 1, 2, 3, 4])
                
    def test_case_3(self):
        result = solution.quick_sort([3, 1, 5, 6])
        self.assertEqual(result, [1, 3, 5, 6])

    def test_case_4(self):
        result = solution.merge_sort([3, 1, 5, 6])
        self.assertEqual(result, [1, 3, 5, 6])

if __name__ == '__main__':
    unittest.main()