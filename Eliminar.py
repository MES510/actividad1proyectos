# Librerias
import re
import os
import time

class Eliminar:
    def remover_Etiquetas(self):
        #Ruta
        path = r"D:/Jose/Documents/Actividad1/Files"
        pathS = r'D:/Jose/Documents/Actividad1/Textos'

        os.chdir(path)



        # Funcion para eliminar las etiquetas HTML
        def eliminar_tags(value):
            return re.sub(r'<[^>]*?>', '', value)


        contador = 0o01
        inicioTotal = time.time()
        for archivos in os.listdir():
            inicio = time.time()
            if archivos.endswith(".html"):
                #datos_path = f"{pathS}\{archivos}"
                archivo =  open(archivos, 'r' ,encoding="unicode_escape")
                archivo_Ac = archivo.read()

                nuevo = open(f"{pathS}/{contador}.txt", 'w', encoding="utf-8")
                nuevo.write(eliminar_tags(archivo_Ac))
                nuevo.close()
                contador += 1
                fin = time.time()
                print(f'El tiempo total en eliminar las etiquetas del archivo {archivos} fue: '+ str(round(fin-inicio, 3)))
        finalTotal = time.time()
        print()
        print('El tiempo total de ejecución fue: '+ str(round(finalTotal-inicioTotal, 2)))

        return
