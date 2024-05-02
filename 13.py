class ClassA:
  def __init__(self):
    self.a = 'hello'
#継承ってなんだよ

class ClassB(ClassA):
  def get_class_a(self):
    return self.a  #オリジナルのインスタンス変数を返す？インスタンスは一個一個のデータのセットのことだろ

