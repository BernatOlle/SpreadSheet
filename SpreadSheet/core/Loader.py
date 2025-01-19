import csv
from SpreadSheet.MenuManager.UserInterface import UserInterface
from SpreadSheet.Evaluators.FormulaComputing import FormulaComputing
class Loader():

    def __init__(self, formulacomputing):
        self.MainMenu = UserInterface()
        self.formulacomputing = formulacomputing

    def loadSpreadSheet(self, path):
        cells = {}
        # Abrir el archivo y leer las líneas
        with open(path, 'r') as file:
            lines = file.readlines()

        # Procesar cada línea del archivo
        for row_idx, line in enumerate(lines):
            columns = line.strip().split(';')  # Dividir cada línea en columnas separadas por ';'
            for col_idx, value in enumerate(columns):
                if value != '':  # Verificar si el valor es distinto de ';'
                    # Obtener la coordenada correspondiente
                    letra = chr(65 + col_idx)  # Convertir el índice a letra (A, B, C, ...)
                    numero = row_idx + 1  # Sumar 1 para ajustar al número de fila
                    coordenada = f"{letra}{numero}"
                    if value[0] == "=":
                        value = value.replace(",",";")
                    cells[coordenada] = value
        return cells
            
    def loadCommands(self,name):
        with open(name, 'r') as archivo_csv:
            c = []
            #Lee el fichero linea por linea
            csv_reader = csv.reader(archivo_csv)
            for linea in csv_reader:
                #lineas_csv.append(linea)
                cc = self.MainMenu.mainMenu(linea)
                c.append(cc)
            return c
        
    
    def file_loader(self,namefile, spreadsheet):
        loaded_dic = self.loadSpreadSheet(namefile)
        falta = []
        dic = {}
        for clave, valor in loaded_dic.items():
            try:
                spreadsheet.insertContentInCell(clave,valor)
            except:
                dic[clave] = valor
                falta.append(dic)
                dic = {}
        i = 0

        while len(falta)!=0:
            try:
                print("INSERTO")
                falta_key = list(falta[i].keys())
                falta_value = list(falta[i].values())
                spreadsheet.insertContentInCell(falta_key[0],falta_value[0])
                falta.pop(i)
            except Exception as Err:
                print("NO PUEDO INSERTAR ", Err.__traceback__)
                falta.pop(i)
                
            
               
            i+=1
            if i >= len(falta):
                i = 0 
        return spreadsheet
    