from Content.entities.Content import Content  

class TextContent(Content):
  def __init__(self, content) -> None:
        super().__init__("TextContent", content)
        self.content = content

  def getNumericalValue(self):
        if self.content == "":
            return 0
        else:
            try:
                num_value = float(self.content)
                return num_value
            except:
                raise TextualCellEception("The system tries to get a numerical value from a text value")
        

  def getTextualValue(self):
        return str(self.content)
      
      
      
class TextualCellEception(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)