import unittest
import solution

class temp(unittest.TestCase):
    def test_case_1(self):
        result = solution.solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG'])
        self.assertEqual(result, ['img1.png', 'IMG01.GIF', 'img02.png', 'img2.JPG', 'img10.png', 'img12.png'])

    def test_case_2(self):
        result = solution.solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat'])
        self.assertEqual(result, ['A-10 Thunderbolt II', 'B-50 Superfortress', 'F-5 Freedom Fighter', 'F-14 Tomcat'])

if __name__ == '__main__':
    unittest.main()