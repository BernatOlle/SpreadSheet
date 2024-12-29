class PromedioOperand():
    def __init__(self,args) -> None:
        self.args = args
        super().__init__()
        
          
    
    def getValue(self):
        result = 0
        for arg in self.args:
            val = arg.getValue()
            if arg.isType() == "Cell_Range":
                for i in val:
                    result += i
            else:
                result += val
        
        result = result/len(self.args)
        return result