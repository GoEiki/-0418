from __future__ import annotations
import typing
class Matrix:
  def __init__(self, matrix:list) -> None:
    pass

  # list型を返す
  @property
  def matrix(self) -> list:
    return None
  
  # 和
  def plus(self, m:Matrix) -> typing.Tuple[Matrix]:
    return None
  
  # 差 
  def minus(self, m:Matrix) -> typing.Tuple[Matrix]:
    return None
    
  # アマダール積 and 定数積
  def multiply(self, m:typing.Union[Matrix, int, float]) -> typing.Tuple[Matrix]:
    return None
    
  # 積
  def dot(self, m:Matrix) -> typing.Tuple[Matrix]:
    return None
    
  # 転置
  def T(self) -> Matrix:
    return None
    
  # 行列式
  def det(self) -> typing.Union(int, float):
    return None
    
  # 逆行列
  def inv(self) -> Matrix:
    return None

if __name__ == '__main__':
  pass
