from SpreadSheet.Controller.SpreadSheetController import SpreadSheetManager

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetManager()
    while True:
        
        try:
            spreadsheetcontroller.display_menu()
        except Exception as Error:
            print(Error.message)
        
