D = __import__('14')

import unittest

class Unittest13(unittest.TestCase):
  def test1(self):
    temp = D.ClassD(1, 2)
    self.assertEqual(temp.get_classc_a_b(), 3)
  
  def test2(self):
    temp = D.ClassD(13.2, 5)
    self.assertAlmostEqual(temp.get_classc_a_b(), 18.2)

  def test3(self):
    temp = D.ClassD("hoge", "fuga")
    self.assertEqual(temp.get_classc_a_b(), "hogefuga")

  def test4(self):
    temp = D.ClassD([1, 2], [3, 4])
    self.assertEqual(temp.get_classc_a_b(), [1, 2, 3, 4])


if __name__ == '__main__':
  unittest.main()