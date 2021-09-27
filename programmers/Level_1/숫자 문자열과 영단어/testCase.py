import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution("one4seveneight")
        self.assertEqual(result, 1478)
    
    def test_case_2(self):
        result = solution.solution("23four5six7")
        self.assertEqual(result, 234567)

    def test_case_3(self):
        result = solution.solution("2three45sixseven")
        self.assertEqual(result, 234567)
    
    def test_case_4(self):
        result = solution.solution("123")
        self.assertEqual(result, 123)

if __name__ == '__main__':
    unittest.main()