from Content.entities.Content import Content  
from Content.Manager.ContentManager import ContentManager

class FormulaContent(Content):
    def __init__(self, content, formulaComputing, cells) -> None:
        super().__init__("FormulaContent", content)
        self.contentManager = ContentManager(content, formulaComputing, cells)
        self.content = content

    def calculateFormula(self):
        self.content = self.contentManager.calculateFormulaValue()
    
    def getNumericalValue(self):
        
        return self.content
    
    
    def getTextualValue(self):
        return str(self.content)
    

    def getCircularDependences(self):
        return self.contentManager.dependingCells()    