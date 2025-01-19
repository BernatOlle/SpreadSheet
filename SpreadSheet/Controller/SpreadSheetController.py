# The SpreadSheetManager class handles user commands, checks their syntax,
# and applies corresponding actions to a spreadsheet object.

from UI.UserInterface import UserInterface
from SpreadSheet.entities.SpreadSheet import SpreadSheet
from SpreadSheet.Controller.SpreedSheetCommandException import SpreadSheetCommandException
from SpreadSheet.Evaluators.FormulaComputing import FormulaComputing
from SpreadSheet.core.FileManager import FileManager

class SpreadSheetManager:
    def __init__(self):
        # Set up the user interface, spreadsheet object, formula computation logic, and file handler.
        self.ui_handler = UserInterface()
        self.current_spreadsheet = None
        self.formula_evaluator = FormulaComputing()
        self.file_handler = FileManager(self.formula_evaluator)

    def display_menu(self):
        # Show the main menu to the user and process their command.
        command = self.ui_handler.mainMenu()
        self.process_command(command)

    ##### DISCUSSION: FIRST, WE VALIDATE THE SYNTAX OF THE COMMAND TO BE EXECUTED,
    ##### THEN, WE VERIFY THE LOGIC OF THE CONTROLLER (E.G., EDITING WITHOUT CREATING A FILE IS NOT ALLOWED).

    def process_command(self, command):
        """
        Processes the user's command and executes the appropriate action.

        :param command: A string representing the user's command to be executed.
        The first part of the command determines the type of action (e.g., Edit, Create, Save, etc.).
        """
        print(command)

        if command[0] == 'E':  # Edit a cell
            if self.current_spreadsheet is None:
                raise SpreadSheetCommandException("Cannot edit a cell without creating or loading a spreadsheet.")

            # Add content to the specified cell. Assumes the syntax is valid.
            self.current_spreadsheet.insertContentInCell(cell_id=command[1], content=command[2])
            self.current_spreadsheet.display()  # Display the updated spreadsheet

        elif command[0] == 'C':  # Create a new spreadsheet
            if self.current_spreadsheet and self.current_spreadsheet.getName() == command[1]:
                raise SpreadSheetCommandException("A spreadsheet with the same name already exists.")

            # Create a new spreadsheet instance with the specified name.
            self.current_spreadsheet = SpreadSheet(command[1], self.formula_evaluator)
            print("New spreadsheet created.")

        elif command[0] == 'RF':  # Execute commands from a file
            try:
                command_list = self.file_handler.loadCommands(command[1])
                for single_command in command_list:
                    self.process_command(single_command)
                    self.current_spreadsheet.display()
            except:
                raise SpreadSheetCommandException("Unable to read commands from the specified file.")

        elif command[0] == 'L':  # Load an existing spreadsheet
            try:
                # Extract the file name and load the spreadsheet object.
                filename = command[1].split("/")[-1]
                loaded_spreadsheet = self.file_handler.loadFile(
                    command[1], SpreadSheet(filename, self.formula_evaluator)
                )
                self.current_spreadsheet = loaded_spreadsheet
                self.current_spreadsheet.display()
            except:
                raise SpreadSheetCommandException("Failed to load the specified spreadsheet.")

        elif command[0] == 'S':  # Save the current spreadsheet
            if self.current_spreadsheet is None:
                raise SpreadSheetCommandException("Cannot save a spreadsheet that hasn't been created or loaded.")
            try:
                # Save the current spreadsheet to the specified file.
                self.file_handler.saveFile(self.current_spreadsheet, command[1])
            except:
                raise SpreadSheetCommandException("Failed to save the current spreadsheet.")