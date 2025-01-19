

class Saver():

    def __init__(self) -> None:
        pass

    def saveSpreadSheet(self,spreadsheet, path):
        archivo_txt = path
        cells = spreadsheet.cells
        unique_coordinates = sorted(set(coord[0] for coord in cells.keys()))
        
        lista_completa = [chr(letra) for letra in range(ord(unique_coordinates[0][0]), ord(unique_coordinates[-1][0]) + 1)]

        numbers = sorted(set(int(key[1:]) for key in cells.keys()))
        max_row = max(numbers)
        row = []
        matrix = []
        for i in range(1, max_row+1):
            for col in lista_completa:
                try:
                    touple = col + str(i)
                    val = cells[touple].content.getContent()
                    val = str(val).replace(";",",")
                    val = val + ";"
                except:
                    val = ";"
                    
                row.append(val)
            i = 0
            pos = 0
            for elemento in row:
                if elemento != ';':
                    pos = i  
                i+=1
                
            
            array = row[0:pos+1]
            last_value = array[len(array)-1][:-1]
            array[len(array)-1] = last_value
            matrix.append(array)
            row = []
            
            
        with open(archivo_txt, 'w', newline='') as file:
            # Crear un escritor CSV
            i=0
            
            # Escribir valores
            for row in range(len(matrix)):
                
                i=0
                for col in matrix[row]:
                    file.write(col)
                    if matrix[row] !=";" and len(matrix[row]) < i:
                        file.write(";")   
                    i+=1
                file.write("\n")
                
        print(f'Fila saved in: {archivo_txt}')
