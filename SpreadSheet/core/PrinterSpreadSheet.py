class PrinterSpreadSheet():
    
    def __init__(self) -> None:
        pass

    def ordercells(self, cell_object):
        column, row = cell_object.getCoordinate()
        return column, ord(row)

    def printSpreadSheet(self, celdas, name):
        print("SPREADSHEET NAME: ", name)
        
        # Ordenar las claves del diccionario
        celdas_ordenadas = sorted(celdas.keys())
        # Obtener la lista de columnas distintas
        columnas = []
        max_row = 0
        for cell in celdas_ordenadas:
            column, row = celdas[cell].getCoordinate()
            if column not in columnas:
                columnas.append(column)
            if row > max_row:
                max_row = row
                
        # Imprimir encabezados de columnas
        print("        |", end="")
        for col in columnas:
            print(f"     {col}        |", end="")
        print("\n--------|", end="")
        for _ in range(len(columnas)):
            print("--------------|", end="")
        print()
        
        # Generar tabla con celdas vacías
        for fila in range(1, max_row + 1):
            print(f"{fila:<8}|", end="")
            for col in columnas:
                coordenada = f"{col}{fila}"
                if coordenada in celdas:
                    content = celdas[coordenada].content.getTextualValue()
                    print(f"   {content}         |", end="")
                else:
                    print(f"              |", end="")
            print("\n--------|", end="")
            for _ in range(len(columnas)):
                print("--------------|", end="")
            print()