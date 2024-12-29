import Operand
from Function.Arguments import Arguments
class RangeCells(Operand, Arguments):
    
    def __init__(self, cell1, cells) -> None:
      
        self.cell1 = cells[cell1] #falta añadir excepcion
        
        self.cells = cells
        Arguments.super().__init__("CellReference")
        Operand.super().__init__("CellReference")
      
        
    def getValue(self):
        return self.cell1.content.getNumericalValue()
    
    def getCells(self):
        return self.cell1