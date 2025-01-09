from Content.entities.Content import Content  
from Content.Components.Component import Component

class FormulaContent(Content):
    def __init__(self, content, formulaComputing, cells) -> None:
        super().__init__("FormulaContent", content)
        self.Component = Component(content, formulaComputing, cells)
        self.content = content

    def calculateFormula(self):
        self.content = self.Component.calculateFormulaValue()
    
    def getNumericalValue(self):
        
        return self.content
    
    
    def getTextualValue(self):
        return str(self.content)
    

    def getCircularDependences(self):
        return self.Component.dependingCells()    