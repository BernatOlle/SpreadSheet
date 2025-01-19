from SpreadSheet.MenuManager.UserInterface import UserInterface
from SpreadSheet.entities.SpreadSheet import SpreadSheet
from SpreadSheet.Controller.SpreedSheetCommandException import SpreadSheetCommandException
from SpreadSheet.Evaluators.FormulaComputing import FormulaComputing
from SpreadSheet.core.FileManager import FileManager

class SpreadSheetManager:
    def __init__(self):
        self.ui_handler = UserInterface()
        self.current_spreadsheet = None
        self.formula_evaluator = FormulaComputing()
        self.file_handler = FileManager(self.formula_evaluator)

    def display_menu(self):
        command = self.ui_handler.mainMenu()
        self.process_command(command)

    def process_command(self, command):

        print(command)

        if command[0] == 'E': 
            if self.current_spreadsheet is None:
                raise SpreadSheetCommandException("Cannot edit a cell without creating or loading a spreadsheet.")

            self.current_spreadsheet.insertContentInCell(cell_id=command[1], content=command[2])
            self.current_spreadsheet.display() 

        elif command[0] == 'C':
            if self.current_spreadsheet and self.current_spreadsheet.getName() == command[1]:
                raise SpreadSheetCommandException("A spreadsheet with the same name already exists.")

            self.current_spreadsheet = SpreadSheet(command[1], self.formula_evaluator)
            print("New spreadsheet created.")

        elif command[0] == 'RF': 
            try:
                command_list = self.file_handler.loadCommands(command[1])
                for single_command in command_list:
                    self.process_command(single_command)
                    self.current_spreadsheet.display()
            except:
                raise SpreadSheetCommandException("Unable to read commands from the specified file.")

        elif command[0] == 'L':  
            try:
                filename = command[1].split("/")[-1]
                loaded_spreadsheet = self.file_handler.loadFile(
                    command[1], SpreadSheet(filename, self.formula_evaluator)
                )
                self.current_spreadsheet = loaded_spreadsheet
                self.current_spreadsheet.display()
            except:
                raise SpreadSheetCommandException("Failed to load the specified spreadsheet.")

        elif command[0] == 'S':  
            if self.current_spreadsheet is None:
                raise SpreadSheetCommandException("Cannot save a spreadsheet that hasn't been created or loaded.")
            try:
                self.file_handler.saveFile(self.current_spreadsheet, command[1])
            except:
                raise SpreadSheetCommandException("Failed to save the current spreadsheet.")