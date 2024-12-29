from Content.Components.Operand.Operand import Operand
from Content.Components.Operand.Function.Arguments import Arguments

class Number(Operand,Arguments):
  def __init__(self,value) ->None:
    Operand.__init__(self,"Number")
    Arguments.__init__(self,"Number")
    self.value = value
    
  def getValue(self):
    return float(self.value)