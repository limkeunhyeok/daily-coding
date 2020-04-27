import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(
            [[1, 0, 0, 1, 1, 0],
            [1, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1]], [0, 0], [0, 4])
        self.assertEqual(result, 8)
                
    def test_case_2(self):
        result = solution.solution(
            [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], 
            [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],  
            [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],  
            [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],  
            [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],  
            [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],  
            [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],  
            [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],  
            [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]], [0, 0], [3, 4])
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()