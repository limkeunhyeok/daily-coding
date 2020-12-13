import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF'])
        self.assertEqual(result, 'HELLO')
    
    def test_case_2(self):
        result = solution.solution('CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B'])
        self.assertEqual(result, 'FOO')

    def test_case_3(self):
        result = solution.solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF'])
        self.assertEqual(result, 'WORLD')

if __name__ == '__main__':
    unittest.main()