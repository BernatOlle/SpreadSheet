class MaxOperand():
    def __init__(self, args) -> None:
        self.args = args
        
    
    def getValue(self):
        result = 0
        for arg in self.args:
            val = arg.getValue()
            if arg.isType() == "Cell_Range":
                for i in val:
                    if i >= result:
                        result = i
            else:
                if val >= result:
                    result = val
        return result