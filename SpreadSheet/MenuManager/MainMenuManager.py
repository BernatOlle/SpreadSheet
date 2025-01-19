from SpreadSheet.MenuManager.SyntexException import SyntaxException
import os

class MainMenuManager:
   
    def __init__(self) -> None:
        pass
    
    def mainMenu(self, choice=None):
        print(30 * "-", "MAIN MENU", 30 * "-")
        print("")
        print("COMMANDS ALLOWED:")
        print("RF <text file pathname>         - Read commands from file")
        print("C <file.s2v>                    - Create a new empty spreadsheet")
        print("E <cell coordinate> <new cell content> - Edit a cell")
        print("L <s2v file pathname>           - Load a spreadsheet from file")
        print("S <s2v place pathname>          - Save the spreadsheet to location with the spreadsheet name provided in the creation")
        print("SHOW                            - Shows current spreadsheet")
        print("EXIT                            - Exit the program")
        print(60 * "-")
        print("Examples for 'E' command:")
        print("E A1 7.5            -> to input numeric content")
        print("E B2 I am a text    -> to input text content")
        print("E C3 =A1+7          -> to input formula content")
        print(60 * "-")
        print("")
        
        if choice is not None:
            return self.insertCommand(choice)
        else:
            return self.insertCommand()

    def insertCommand(self, choice=None):
        """
        The function prompts the user for a command, passes it to a command syntax checker, and then applies
        the command.
        """
        if choice is not None:
            choice = str(choice).replace('[', '').replace(']', '').replace("'", '')
            parsed_choice = self.commandSyntax(choice)
        else:
            choice = input("ENTER A COMMAND: ")
            parsed_choice = self.commandSyntax(choice)
        return parsed_choice

    def commandSyntax(self, command): 
        try:
            parsed_command = command.split(" ")
        except Exception:
            raise SyntaxException("Can't not parse the command")
        
        # Añadimos "EXIT" al conjunto de comandos permitidos
        if parsed_command[0] not in {"RF", "C", "E", "L", "S", "EXIT", "SHOW"}:
            raise SyntaxException("Command not correct")
        
        if parsed_command[0] == "EXIT":
            return ("EXIT",)
        
        if parsed_command[0] == "SHOW":
            return ("SHOW",)

        if parsed_command[0] == "E":
            if len(parsed_command) < 3:
                raise SyntaxException("Parsing Error, you need to specify CELL ID and CONTENT (EXAMPLE: E A4 4.5)")
            cell_id = parsed_command[1]
            self.idCellSyntaxControl(cell_id)
            content = " ".join(parsed_command[2:])
            return ("E", cell_id, content)

        if parsed_command[0] == "C":
            if len(parsed_command) != 2:
                raise SyntaxException("Command C does not require additional arguments. Just type C 'filename.s2v'.")
            return ("C", parsed_command[1])

        if parsed_command[0] == "RF":
            if len(parsed_command) != 2:
                raise SyntaxException("RF command requires exactly one argument (example: RF file.txt)")
            if not self.pathExists(parsed_command[1]):
                raise SyntaxException("THE PATH DOESN'T EXIST")
            return ("RF", parsed_command[1])

        if parsed_command[0] == "L":
            if len(parsed_command) != 2:
                raise SyntaxException("L command requires exactly one argument (example: L SpreadSheet.s2v)")
            if not self.pathExists(parsed_command[1]):
                raise SyntaxException("THE PATH DOESN'T EXIST")
            return ("L", parsed_command[1])

        if parsed_command[0] == "S":
            if len(parsed_command) != 2:
                raise SyntaxException("S command requires exactly one argument (example: S SpreadSheet.s2v)")
            return ("S", parsed_command[1])
    
    def idCellSyntaxControl(self, cell_id):
        for char in cell_id:
            if not (char.isdigit() or char.isalpha()):
                raise SyntaxException("The ID of the CELL contains a non-alphanumerical value")
            
        i = 0
        while i < len(cell_id) and cell_id[i].isalpha():
            i += 1
        
        if i == 0 or i == len(cell_id) or not cell_id[i:].isdigit():
            raise SyntaxException("The order of the cell ID is not correct, remember (first letters and then numbers)")
        
    def pathExists(self, path):
        directorio = os.path.dirname(path)
        if directorio == "":
            return True
        return os.path.exists(directorio)
