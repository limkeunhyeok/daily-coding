import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution('FRANCE', 'french')
        self.assertEqual(result, 16384)

    def test_case_2(self):
        result = solution.solution('handshake', 'shake hands')
        self.assertEqual(result, 65536)

    def test_case_3(self):
        result = solution.solution('aa1+aa2', 'AAAA12')
        self.assertEqual(result, 43690)

    def test_case_4(self):
        result = solution.solution('E=M*C^2', 'e=m*c^2')
        self.assertEqual(result, 65536)

if __name__ == '__main__':
    unittest.main()