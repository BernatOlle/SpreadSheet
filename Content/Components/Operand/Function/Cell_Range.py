from Content.Components.Operand.Operand import Operand
from Content.Components.Operand.Function.Arguments import Arguments

class Cell_Range(Operand, Arguments):
    #solo rowa y rowb
    def __init__(self, cell1, cell2, cells) -> None:
        column_a = ""
        row_a = ""
        column_b = ""
        row_b = ""
        
        for v in cell1:
            if v.isalpha():
                column_a = column_a + v
            elif v.isdigit():
                row_a= row_a+ v
                
        for v in cell2:
            if v.isalpha():
                column_b = column_b + v
            elif v.isdigit():
                row_b = row_b + v
                
        self.row_a = int(row_a)
        self.column_a = column_a
        
        self.row_b = int(row_b)
        self.column_b = column_b
        
        self.cells = cells
       
        
        Operand.__init__(self,"Cell_Range")
        Arguments.__init__(self,"Cell_Range")
        
    def getValue(self):
      # faltan exepciones
        range_values = []
        
        
        for cell in self.cells.values():
                if cell.column >= self.column_a and cell.column <=self.column_b:
                    if cell.row >= self.row_a and cell.row <= self.row_b:
                        range_values.append(cell.content.getNumericalValue())
        if len(range_values) == 0:
            return [0]   
        return range_values
    
    def getCells(self):
        range_cells = []

        # Crear un conjunto de todas las celdas existentes en self.cells
        existing_cells = {f"{cell.column}{cell.row}" for cell in self.cells.values()}

        # Iterar sobre el rango especificado por column_a, column_b, row_a, row_b
        for col in range(ord(self.column_a), ord(self.column_b) + 1):  # Columnas como letras
            for row in range(self.row_a, self.row_b + 1):  # Filas como números
                cell_id = f"{chr(col)}{row}"  # Crear la celda como string, por ejemplo, "A1"
                
                if cell_id in existing_cells:
                    # Añadir celdas existentes como objetos
                    cell_obj = next(cell for cell in self.cells.values() if f"{cell.column}{cell.row}" == cell_id)
                    range_cells.append(cell_obj)
                else:
                    # Añadir celdas faltantes como cadenas de texto
                    range_cells.append(cell_id)

        return range_cells