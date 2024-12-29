class Content():
    def __init__(self, type, contentText) -> None:
        super().__init__()
        self.type =type
        self.contentText = contentText

    def getNumericalValue(self):
        pass

    def getTextualValue(self):
        pass
    
    def getContent(self):
        return self.contentText
    
    def typeOfContent(self):
        return self.type