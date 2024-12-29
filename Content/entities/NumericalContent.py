from Content.entities.Content import Content  

class NumericalContent(Content):
    def __init__(self, content) -> None:
        super().__init__("NumericalContent", content)
        self.content = content

    def getNumericalValue(self):
        return float(self.content)

    def getTextualValue(self):
        return str(self.content)
