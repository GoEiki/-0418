class ClassC:
  def __init__(self, a, b):
    self.a = a
    self.b = b

class ClassD(ClassC):
  def __init__(self,a,b):
    super().__init__(a,b)
  def get_classc_a_b(self,a,b):
      return self.a+self.b