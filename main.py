from SpreadSheet.Controller.SpreadSheetController import SpreadSheetManager

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetManager()
    while True:
        
        try:
            if not spreadsheetcontroller.display_menu():
                break
        except Exception as Error:
            print(Error.message)
        
