import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('3people unFollowed me')
        self.assertEqual(result, "3people Unfollowed Me")

    def test_case_2(self):
        result = solution.solution("for the last week")
        self.assertEqual(result, "For The Last Week")

if __name__ == '__main__':
    unittest.main()