import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
        self.assertEqual(result, ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])

if __name__ == '__main__':
    unittest.main()