import matrix

import unittest

class UnittestMatrix(unittest.TestCase):
  # 今回テストで使用する行列
  def setUp(self):
    self.a = [[1, 2], [3, 4]]
    self.b = [[2, 5.2], [-6, 1]]
    self.c = [[1, 3, 2], [4, 5, 6]]
    self.d = [[6, 5], [-10, 2.2], [-5, -44]]
    self.e = [[5, 6, 4], [2, 3, -8], [5, -6, 9]]
    self.f = [1, 2]
    self.g = [[-5], [6]]
    self.h = 5
    self.i = [[5, 8, 8.5], [2, 5/3, -4], [0, 5, 10]]
    self.j = [6, -5.2]
    self.k = [[1, 3, 5], [-1, 1, 3], [-1, 1, 3]]
    self.l = [[1, -2, 3, -4], [-5, -6, 7, 8], [-9, 10, -11, 12], [13, 14, -15, -16]]

  # インスタンスのテスト
  def test_correct_input(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    c_m = matrix.Matrix(self.c)
    d_m = matrix.Matrix(self.d)
    e_m = matrix.Matrix(self.e)
    f_m = matrix.Matrix(self.f)
    g_m = matrix.Matrix(self.g)
    h_m = matrix.Matrix(self.h)
    i_m = matrix.Matrix(self.i)
    j_m = matrix.Matrix(self.j)
    k_m = matrix.Matrix(self.k)
    l_m = matrix.Matrix(self.l)
    self.assertEqual(a_m.matrix, self.a)
    self.assertEqual(b_m.matrix, self.b)
    self.assertEqual(c_m.matrix, self.c)
    self.assertEqual(d_m.matrix, self.d)
    self.assertEqual(e_m.matrix, self.e)
    try:
      self.assertEqual(f_m.matrix, self.f)
    except:
      self.assertEqual(f_m.matrix, [self.f])
    self.assertEqual(g_m.matrix, self.g)
    try:
      self.assertEqual(h_m.matrix, self.h)
    except:
      self.assertEqual(h_m.matrix, [[self.h]])
    self.assertEqual(i_m.matrix, self.i)
    try:
      self.assertEqual(j_m.matrix, self.j)
    except:
      self.assertEqual(j_m.matrix, [self.j])
    self.assertEqual(k_m.matrix, self.k)
    self.assertEqual(l_m.matrix, self.l)

  # 行列が定義できない入力に対してのテスト
  def test_wrong_input(self):
    with self.assertRaises(ValueError):
      matrix.Matrix([[1, 2],[5]])
    with self.assertRaises(ValueError):
      matrix.Matrix([[2.6, 5], [4, -6], [-5, 2]])
    a_m = matrix.Matrix(self.a)

  # 和のテスト
  def test_plus(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    e_m = matrix.Matrix(self.e)
    f_m = matrix.Matrix(self.f)
    i_m = matrix.Matrix(self.i)
    j_m = matrix.Matrix(self.j)
    self.assertAlmostEqual(a_m.plus(b_m).matrix, [[3, 7.2], [-3, 5]], places=3)
    self.assertAlmostEqual(b_m.plus(a_m).matrix, [[3, 7.2], [-3, 5]], places=3)
    self.assertAlmostEqual(a_m.plus(b_m).plus(b_m).matrix, [[5, 12.4], [-9, 6]], places=3)
    try:
      self.assertEqual(f_m.plus(j_m).matrix, [7, -3])
    except:
      self.assertEqual(f_m.plus(j_m).matrix, [[7, -3]])
    self.assertAlmostEqual(e_m.plus(i_m).matrix, [[10, 14, 12.5], [4, 4.666666667, -12], [5, -1, 19]], places=3) 
    # ちょっぴりいじわるかもしれない
    self.assertEqual(a_m.matrix, self.a)

  # 和が計算不可能な入力に対してのテスト
  def test_wrong_plus(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    c_m = matrix.Matrix(self.c)
    e_m = matrix.Matrix(self.e)
    g_m = matrix.Matrix(self.g)
    with self.assertRaises(ValueError):
      a_m.plus(c_m)
    with self.assertRaises(ValueError):
      a_m.plus(g_m)
    with self.assertRaises(ValueError):
      e_m.plus(b_m)

  # 差のテスト
  def test_minus(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    e_m = matrix.Matrix(self.e)
    f_m = matrix.Matrix(self.f)
    i_m = matrix.Matrix(self.i)
    j_m = matrix.Matrix(self.j)
    self.assertAlmostEqual(a_m.minus(b_m).matrix, [[-1.0, -3.2], [9.0, 3.0]], places=3)
    self.assertAlmostEqual(b_m.minus(a_m).matrix, [[1.0, 3.2], [-9.0, -3.0]], places=3)
    self.assertAlmostEqual(a_m.minus(b_m).minus(b_m).matrix, [[-3.0, -8.4], [15.0, 2.0]], places=3)
    try:
      self.assertEqual(f_m.minus(j_m).matrix, [-5, 7])
    except:
      self.assertEqual(f_m.minus(j_m).matrix, [[-5, 7]])
    self.assertAlmostEqual(i_m.minus(e_m).matrix, [[0.0, 2.0, 4.5], [0.0, -1.3333333333333333, 4.0], [-5.0, 11.0, 1.0]], places=3) 
    # ちょっぴりいじわるかもしれない
    self.assertEqual(a_m.matrix, self.a)

  # 差が計算不可能な入力に対してのテスト
  def test_wrong_minus(self):
    a_m = matrix.Matrix(self.a)
    d_m = matrix.Matrix(self.d)
    g_m = matrix.Matrix(self.g)
    i_m = matrix.Matrix(self.i)
    with self.assertRaises(ValueError):
      a_m.minus(d_m)
    with self.assertRaises(ValueError):
      a_m.minus(g_m)
    with self.assertRaises(ValueError):
      i_m.minus(a_m)
    
  # アマダール積が計算のテスト
  def test_multiply(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    e_m = matrix.Matrix(self.e)
    f_m = matrix.Matrix(self.f)
    i_m = matrix.Matrix(self.i)
    self.assertAlmostEqual(a_m.multiply(b_m).matrix, [[2, 10.4], [-18, 4]], places=3)
    self.assertAlmostEqual(i_m.multiply(e_m).matrix, [[ 25,  48,  34], [  4,   5,  32], [  0, -30,  90]], places=3)
    try:
      self.assertAlmostEqual(f_m.multiply(i_m).matrix, [6, -10], places=3)
    except:
      self.assertAlmostEqual(f_m.multiply(i_m).matrix, [[6, -10]], places=3)
    # ちょっぴりいじわるかもしれない
    self.assertEqual(a_m.matrix, self.a)
  
  # アマダール積が計算不可能な入力に対してのテスト
  def test_wrong_multiply(self):
    a_m = matrix.Matrix(self.a)
    c_m = matrix.Matrix(self.c)
    d_m = matrix.Matrix(self.d)
    f_m = matrix.Matrix(self.f)
    i_m = matrix.Matrix(self.i)
    j_m = matrix.Matrix(self.j)
    with self.assertRaises(ValueError):
      a_m.multiply(c_m).matrix
    with self.assertRaises(ValueError):
      d_m.multiply(f_m).matrix
    with self.assertRaises(ValueError):
      i_m.multiply(j_m).matrix

  # 定数積が計算のテスト
  def test_constant_multiply(self):
    a_m = matrix.Matrix(self.a)
    e_m = matrix.Matrix(self.e)
    g_m = matrix.Matrix(self.g)
    self.assertAlmostEqual(a_m.multiply(2).matrix, [[2, 4], [6, 8]], places=3)
    self.assertAlmostEqual(g_m.multiply(-1/3).matrix, [[ 1.66666667], [-2]], places=3)
    self.assertAlmostEqual(e_m.multiply(-5).matrix, [[-25, -30, -20], [-10, -15,  40], [-25,  30, -45]], places=3)
    # ちょっぴりいじわるかもしれない
    self.assertEqual(a_m.matrix, self.a)
  
  # 積のテスト
  def test_dot(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    c_m = matrix.Matrix(self.c)
    d_m = matrix.Matrix(self.d)
    e_m = matrix.Matrix(self.e)
    g_m = matrix.Matrix(self.g)
    self.assertAlmostEqual(a_m.dot(b_m).matrix, [[-10.0, 7.2], [-18.0, 19.6]], places=3)
    self.assertAlmostEqual(b_m.dot(a_m).matrix, [[17.6, 24.8], [-3.0, -8.0]], places=3)
    self.assertAlmostEqual(c_m.dot(d_m).matrix, [[-34.0, -76.4], [-56.0, -233.0]], place=3)
    self.assertAlmostEqual(c_m.dot(e_m).matrix, [[21, 3, -2], [60, 3, 30]], places=3)
    self.assertAlmostEqual(b_m.dot(g_m).matrix, [[21.2], [36.0]], places=3)
    # ちょっぴりいじわるかもしれない
    self.assertEqual(a_m.matrix, self.a)
  
  # 積が計算不可能な入力に対してのテスト
  def test_wrong_dot(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    d_m = matrix.Matrix(self.d)
    g_m = matrix.Matrix(self.g)
    i_m = matrix.Matrix(self.i)
    j_m = matrix.Matrix(self.j)
    with self.assertRaises(ValueError):
      a_m.dot(d_m)
    with self.assertRaises(ValueError):
      i_m.dot(j_m)
    with self.assertRaises(ValueError):
      b_m.dot(g_m)

  # 転置のテスト
  def test_T(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    e_m = matrix.Matrix(self.e)
    i_m = matrix.Matrix(self.i)
    self.assertAlmostEqual(a_m.T().matrix, [[1, 3], [2, 4]], places=3)
    self.assertAlmostEqual(b_m.T().matrix, [[2.0, -6.0], [5.2, 1.0]], places=3)
    self.assertAlmostEqual(e_m.t().matrix, [[5, 2, 5], [6, 3, -6], [4, -8, 9]], places=3)
    self.assertAlmostEqual(i_m.t().matrix, [[5.0, 2.0, 0.0], [8.0, 1.6666666666666667, 5.0], [8.5, -4.0, 10.0]], places=3)

  # 転置が計算不可能な行列に対してのテスト
  def test_wrong_T(self):
    c_m = matrix.Matrix(self.c)
    d_m = matrix.Matrix(self.d)
    g_m = matrix.Matrix(self.g)
    with self.assertRaises(ValueError):
      c_m.t()
    with self.assertRaises(ValueError):
      d_m.t()
    with self.assertRaises(ValueError):
      g_m.t()
  
  # 行列式のテスト
  def test_det(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    e_m = matrix.Matrix(self.e)
    h_m = matrix.Matrix(self.h)
    k_m = matrix.Matrix(self.k)
    l_m = matrix.Matrix(self.l)
    self.assertAlmostEqual(a_m.det(), -2, places=3)
    self.assertAlmostEqual(b_m.det(), 33.2, places=3)
    self.assertAlmostEqual(e_m.det(), -561, places=3)
    self.assertAlmostEqual(k_m.det(), 0, places=3)
    self.assertAlmostEqual(h_m.det(), 5, places=3)
    self.assertAlmostEqual(l_m.det(), -768, places=3)
  
  # 行列式が計算不可能な行列に対してのテスト
  def test_wrong_det(self):
    c_m = matrix.Matrix(self.c)
    d_m = matrix.Matrix(self.d)
    j_m = matrix.Matrix(self.j)
    with self.assertRaises(ValueError):
      c_m.det()
    with self.assertRaises(ValueError):
      d_m.det()
    with self.assertRaises(ValueError):
      j_m.det()

  # 逆行列のテスト
  def test_inv(self):
    a_m = matrix.Matrix(self.a)
    b_m = matrix.Matrix(self.b)
    i_m = matrix.Matrix(self.i)
    l_m = matrix.Matrix(self.l)
    self.assertAlmostEqual(a_m.inv(), [[-2, 1], [1.5, -0.5]], places=3)
    self.assertAlmostEqual(b_m.inv(), [[0.030120481927710843, -0.1566265060240964], [0.18072289156626506, 0.060240963855421686]], places=3)
    self.assertAlmostEqual(i_m.inv(), [[0.3384615384615385, -0.34615384615384626, -0.42615384615384627], [-0.18461538461538463, 0.4615384615384616, 0.34153846153846157], [0.09230769230769231, -0.23076923076923078, -0.07076923076923078]], places=3)
    self.assertAlmostEqual(l_m.inv(), [[-0.25, 0.33333333333333326, -0.08333333333333333, 0.16666666666666657], [0.6875, 0.9375, 0.1875, 0.4375], [0.625, 0.875, 0.125, 0.375], [-0.1875, 0.27083333333333337, -0.020833333333333332, 0.10416666666666669]], places=3)

  # 逆行列が計算不可能な行列に対してのテスト
  def test_wrong_inv(self):
    f_m = matrix.Matrix(self.f)
    g_m = matrix.Matrix(self.g)
    k_m = matrix.Matrix(self.k)
    with self.assertRaises(ValueError):
      f_m.inv()
    with self.assertRaises(ValueError):
      g_m.inv()
    with self.assertRaises(ValueError):
      k_m.inv()

if __name__ == '__main__':
  unittest.main()