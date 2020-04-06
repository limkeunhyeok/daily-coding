import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('1->2->3->4->5', 2)
        self.assertEqual(result, '1->2->3->5')
                
    def test_case_2(self):
        result = solution.solution('1->2->3', 3)
        self.assertEqual(result, '2->3')
    
    def test_case_3(self):
        result = solution.solution('1', 1)
        self.assertEqual(result, 'Null')

if __name__ == '__main__':
    unittest.main()