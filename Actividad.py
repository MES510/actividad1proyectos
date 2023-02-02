import os
import time

# Clase
class LeerArchivos:

    def Ejecucion(self):

        #Ruta de los archivos
        path = r"D:/Jose/Documents/Actividad1/Files"
        # Abrir Archivo
        os.chdir(path)
        
        suma = 0 

        inicioTotal = time.time()

        
        #leer los archivos
        def leer_archivos(archivos_path):
            with open(archivos_path, 'r', encoding="unicode_escape") as f:
                print(f.name)
                f.read()
                
        #Iterar en los archivos
        for datos in os.listdir():
            inicio = time.time()
            if datos.endswith(".html"):
                datos_path = f"{path}\{datos}"
                leer_archivos(datos_path) 
                   
            print()
            fin = time.time()
            print('El tiempo de lectura fue: '+ str(round(fin-inicio, 5)))
            suma = round(fin-inicio, 5) + suma

        finTotal = time.time()

        print('Tiempo total de ejecución de los archivos en segundos '+str(round(suma,3)))
        print('Tiempo total de ejecución en segundos '+str(round(finTotal-inicioTotal,2)))

        return




