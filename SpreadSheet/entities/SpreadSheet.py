# The SpreadSheet class represents a spreadsheet and allows for inserting content into cells and
# printing the spreadsheet.

from SpreadSheet.entities.Cell import Cell
from SpreadSheet.core.PrinterSpreadSheet import PrinterSpreadSheet



class SpreadSheet:
    
    def __init__(self, name, formulaComputing):
        self.name = name
        self.cells = {}
        self.no_existent_cells = {}
        self.printSpreadSheet = PrinterSpreadSheet()
        self.formulaComputing = formulaComputing
  
    
    def getName(self):
        return self.name
   
    def insertContentInCell(self, cell_id, content):
        if len(self.cells)==0 or not cell_id in self.cells:
            cell = Cell(cell_id, self.formulaComputing, self)
               
        else:
            cell = self.cells[cell_id]
        
        self.cells[cell_id] = cell
        cell.insertCellContent(content)
        
        
    def display(self):
        self.printSpreadSheet.printSpreadSheet(self.cells, self.name)


