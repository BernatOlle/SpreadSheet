from .Tokenize import Tokenize
from .Parser import Parser
from .GeneratePostfix import GeneratePostfix
class FormulaComputing():
    def __init__(self) -> None:
        self.tokenize = Tokenize()
        self.parse = Parser()
        self.generatePostfix = GeneratePostfix()
        
    def computeFormula(self, string):
        token_list = self.tokenize.tokenize(string)
        parsed_list = self.parse.parse(token_list)
        postfix = self.generatePostfix.infixToPostfix(parsed_list)
        return postfix
        
