import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
        self.assertEqual(result, [3, 3])
    
    def test_case_2(self):
        result = solution.solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
        self.assertEqual(result, [0, 0])
        
    def test_case_3(self):
        result = solution.solution(2, 	["hello", "one", "even", "never", "now", "world", "draw"])
        self.assertEqual(result, [1, 3])
                
if __name__ == '__main__':
    unittest.main()