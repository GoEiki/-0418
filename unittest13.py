B = __import__('13')

import unittest

class Unittest13(unittest.TestCase):
  def test1(self):
    class_b = B.ClassB()
    self.assertEqual(class_b.get_class_a(), "hello")

if __name__ == '__main__':
  unittest.main()