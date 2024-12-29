from Content.entities.Content import Content
from Content.entities.NumericalContent import NumericalContent
from Content.entities.TextContent import TextContent
from Content.entities.FormulaContent import FormulaContent
from SpreadsheetMarkerForStudents.entities.circular_dependency_exception import CircularDependencyException
class Cell:
    ##ME INTERESA GUARDAR POR SEPARADO LAS FILAS Y COLUMNAS PARA PODER PRINTEARLAS MEJOR
    def __init__(self, cell_id, formulaComputing, spreadsheet) -> None:
        column = ""
        row = ""
        self.cell_id = cell_id
        
        for v in cell_id:
            if v.isalpha():
                column = column + v
            elif v.isdigit():
                row= row + v
        self.row = int(row)
        self.column = column
        self.spreadsheet = spreadsheet
        ##DUDA JUAN CARLOS: DUDO MUCHO QUE TE GUSTE ESTO
        self.content : Content
        self.formulaComputing = formulaComputing
        self.iDependOn = []
        self.dependOnMe = {}
    def getCoordinate(self):
        return self.column, self.row
    
    def getContent(self):
        return self.content
    
    def insertNewContent(self, content_string):
        """
        The function `insertNewContent` takes a string as input and returns an instance of a specific
        content type (FormulaContent, NumericalContent, or TextualContent) based on the content of the
        string.
        
        :param content_string: The `content_string` parameter is a string that represents the content you
        want to insert. It can be either a numerical value (integer or float) or a textual value (string)
        :return: an instance of either the FormulaContent, NumericalContent, or TextualContent class,
        depending on the type of content_string passed as a parameter.
        """
    
        string = content_string.strip()
        if string[0] == "=":
            formulacontent = FormulaContent(content_string, self.formulaComputing, self.spreadsheet.cells)
            self.proveNoCircularExeption(content_string)
            formulacontent.calculateFormula() #LE PASARIA SOLO LAS DEPENDING CELLS PERO TENGO PROBLEMAS CON LAS OPERACIONES CON RANGOS NO SON SOLO UNA CELDA
            newdepend = formulacontent.getCircularDependences()
            
            if self.cell_id in self.spreadsheet.no_existent_cells:
                depend_cell = self.spreadsheet.no_existent_cells.pop(self.cell_id)
                self.dependOnMe[depend_cell.cell_id] = depend_cell
        
            
            for cell_depend in newdepend:
                if not isinstance(cell_depend, str):
                    cell_depend.dependOnMe[self.column + str(self.row)] = self
                else:
                    self.spreadsheet.no_existent_cells.update({cell_depend:self})
                    
            
            if len(self.dependOnMe) != 0:
                eliminar = set(self.dependOnMe) - set(newdepend)
            else:
                eliminar = set()
            
            self.iDependOn = newdepend
            
            self.setDependOnMe(list(eliminar))

            self.content = formulacontent
        else:
            try:
                
                self.content = NumericalContent(content_string)
                
            except:
                self.content = TextContent(content_string)
        
            
        
        if len(self.dependOnMe)!=0:
            for cell in self.dependOnMe.values():
                cell.recalculateFormula()
                
                

    def recalculateFormula(self):
        try:
            self.content.calculateFormula()     
        except:
            raise CircularDependencyException("")
        
    def setDependOnMe(self, eliminar):
        if len(self.iDependOn) != 0:
            celda = self.column + str(self.row)
            for cell in self.iDependOn:
                if eliminar != None:
                    for e in eliminar:
                        i = 0
                        for delete in cell.iDependOn:
                            todele = delete.column + str(delete.row)
                            if todele == celda:
                                del cell.iDependOn[i]
                            i=+1
                
                
    def proveNoCircularExeption(self, string):
        if len(self.dependOnMe) != 0:
            postfix = self.formulaComputing.computeFormula(string)
            
            for iscell in postfix:
                a = self.formulaComputing.parse.is_valid_cell(iscell)
                
                if a:
                    idependon = iscell
                    
                    for dependonme in self.dependOnMe.values():
                        dependonme.proveNoCircularExeption(string)
                        dependonmecellid = dependonme.column + str(dependonme.row)
                        
                        if idependon == dependonmecellid:
                            raise CircularDependencyException("ERROR")
    