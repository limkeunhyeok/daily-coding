import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('1->2->3', '1->2->3')
        self.assertEqual(result, '1->1->2->2->3->3')
                
    def test_case_2(self):
        result = solution.solution('1->3->5->6', '2->4')
        self.assertEqual(result, '1->2->3->4->5->6')

if __name__ == '__main__':
    unittest.main()