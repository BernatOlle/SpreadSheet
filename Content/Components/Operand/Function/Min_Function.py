class MinOperand():
    def __init__(self,args) -> None:
        self.args = args
        
    
    def getValue(self):
        array = []
        for arg in self.args:
            val = arg.getValue()
            if arg.isType() == "Cell_Range":
                for i in val:
                    array.append(i)
            else:
                array.append(val)
        result = min(array)
        return result