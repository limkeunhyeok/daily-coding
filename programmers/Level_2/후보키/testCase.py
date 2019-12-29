import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()