from Content.Components.Operand.Operand import Operand
from Content.Components.Operand.Function.Arguments import Arguments

class Function (Operand,Arguments):
  def __init__(self, funType) -> None:
      Operand.__init__(self,"Function")
      Arguments.__init__(self,"Function")
      self.funType = funType
      pass
        
  def getValue(self):
    pass