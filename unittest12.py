Score2 = __import__('12')

import unittest

class Unittest10(unittest.TestCase):
  def setUp(self):
    self.yamaguchi = Score2.Score2("yamaguchi", 50, 80, 100)
    self.ishikawa = Score2.Score2("ishikawa", 80, 100, 60)
    self.miyazaki = Score2.Score2("miyazaki", 70, 69, 71)
    self.chiba = Score2.Score2("chiba", 85, 80, 60)
    self.hukushima = Score2.Score2("hukushima", 90, 99, 20)

  def test1(self):
    self.assertEqual(self.yamaguchi.get_highscore_and_lecture(), ("japanese", 100))

  def test2(self):
    self.assertEqual(self.ishikawa.get_highscore_and_lecture(), ("english", 100))

  def test3(self):
    self.assertEqual(self.miyazaki.get_highscore_and_lecture(), ("japanese", 71))

  def test4(self):
    self.assertEqual(self.chiba.get_highscore_and_lecture(), ("math", 85))

  def test5(self):
    self.assertEqual(self.hukushima.get_highscore_and_lecture(), ("english", 99))

if __name__ == '__main__':
  unittest.main()