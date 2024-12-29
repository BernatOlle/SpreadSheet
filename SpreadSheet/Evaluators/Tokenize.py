import re
class Tokenize():
    def __init__(self) -> None:
        
        self.patterns = {
            'operator': r'\+|-|\*|/',
            'cell_identifier': r'[A-Z]+\d+',
            'number': r'\d+',
            'opening_round_bracket': r'\(',
            'closing_round_bracket': r'\)',
            'colon_character': r':',
            'semi_colon_character': r';',
            'comma': r',',
            'function_name': r'SUMA|PROMEDIO|MAX|MIN',  # Añadir más funciones según sea necesario
            'range': r'[A-Z]+\d+:[A-Z]+\d+'  # Por ejemplo, A1:B3
        }
    
    def tokenize(self, formula):
        combined_pattern = '|'.join(f'({pattern})' for pattern in self.patterns.values())
        tokens = re.findall(combined_pattern, formula)
        tokens = [token for token in sum(tokens, ()) if token != '']
        return tokens
