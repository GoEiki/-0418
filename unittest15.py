E = __import__('15')

import unittest

class Unittest13(unittest.TestCase):
  def test1(self):
    temp = E.ClassE(1)
    temp.append(2)
    self.assertEqual(temp, [2])
  
  def test2(self):
    temp = E.ClassE(0.2)
    temp.append(0.3)
    temp.append(0.5)
    with self.assertRaises(TypeError):
      temp.append(1)
    self.assertEqual(temp, [0.3, 0.5])
  
  def test3(self):
    temp = E.ClassE([1, 2])
    temp.append([[2, 5], [3, 6]])
    temp.append([7, 15.2, 5])
    with self.assertRaises(TypeError):
      temp.append(1)
    self.assertEqual(temp, [[[2, 5], [3, 6]], [7, 15.2, 5]])
  
  def test4(self):
    temp = E.ClassE(1)
    with self.assertRaises(TypeError):
      temp.append([[2, 5], [3, 6]])
      temp.append((15.2, 69))
    self.assertEqual(temp, [])

if __name__ == '__main__':
  unittest.main()