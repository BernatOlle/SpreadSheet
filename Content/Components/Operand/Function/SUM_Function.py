
from Content.Components.Operand.Function.Function import Function
class SUM_Function(Function):
    def __init__(self, args) -> None:
      super().__init__("SUM")
      self.args = args
        
    def getValue(self):
        result = 0
        for arg in self.args:
            val = arg.getValue()
            if arg.isType() == "Cell_Range":
                for i in val:
                    result += i
            else:
                result += val
        return result
      
      