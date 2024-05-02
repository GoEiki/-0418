Score = __import__('10')
Check = __import__('11')

import unittest

class Unittest11(unittest.TestCase):
  def setUp(self):
    self.yamaguchi = Score.Score("yamaguchi", 50, 80, 100)
    self.ishikawa = Score.Score("ishikawa", 80, 100, 60)
    self.miyazaki = Score.Score("miyazaki", 70, 70, 70)
    self.chiba = Score.Score("chiba", 85, 80, 100)
    self.hukushima = Score.Score("hukushima", 90, 100, 20)

  def test1(self):
    class_list = [self.yamaguchi]
    self.assertEqual(Check.get_math_highscore_student(class_list), "yamaguchi")

  def test2(self):
    class_list = [self.yamaguchi, self.ishikawa]
    self.assertEqual(Check.get_math_highscore_student(class_list), "ishikawa")

  def test3(self):
    class_list = [self.yamaguchi, self.ishikawa, self.miyazaki]
    self.assertEqual(Check.get_math_highscore_student(class_list), "ishikawa")

  def test4(self):
    class_list = [self.yamaguchi, self.ishikawa, self.miyazaki, self.chiba]
    self.assertEqual(Check.get_math_highscore_student(class_list), "chiba")
    
  def test5(self):
    class_list = [self.yamaguchi, self.ishikawa, self.miyazaki, self.chiba, self.hukushima]
    self.assertEqual(Check.get_math_highscore_student(class_list), "hukushima")

if __name__ == '__main__':
  unittest.main()