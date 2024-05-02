Score = __import__('10')

import unittest

class Unittest10(unittest.TestCase):
  def test1(self):
    temp = Score.Score("アイチタロウ", 80, 90, 100)
    self.assertEqual(temp.name, "アイチタロウ")
    self.assertEqual(temp.math, 80)
    self.assertEqual(temp.english, 90)
    self.assertEqual(temp.japanese, 100)

if __name__ == '__main__':
  unittest.main()