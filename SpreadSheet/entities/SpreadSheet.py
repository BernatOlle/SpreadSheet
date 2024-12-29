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
        """
        The function inserts content into a cell if the cell does not already exist.
        
        :param edit_cell: The `edit_cell` parameter is a tuple that contains three elements: `column`,
        `row`, and `content`. The `column` and `row` represent the coordinates of the cell where the content
        will be inserted, and `content` is the actual content that will be inserted into the cell
        """
        
        #crear todas las celdas o nose como hacerlo
        if len(self.cells)==0 or not cell_id in self.cells:
            cell = Cell(cell_id, self.formulaComputing, self)
               
        else:
            cell = self.cells[cell_id]
        
        self.cells[cell_id] = cell
        cell.insertNewContent(content)
        
        
    def display(self):
        self.printSpreadSheet.printSpreadSheet(self.cells, self.name)


