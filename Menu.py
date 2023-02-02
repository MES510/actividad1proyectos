from Actividad import *
from Eliminar import *

opcion = None

while opcion != 4:
    try:
        print()
        print('1. Ver tiempo de ejecucion')
        print('2. Remover etiquetas html')
        print('3. Extraer palabras')
        print('4. Salir')
        opcion = int(input('Seleccione una opcion: '))

        if opcion == 1:
            obj = LeerArchivos()
            obj.Ejecucion()     

        elif opcion == 2:
            obj = Eliminar()
            obj.remover_Etiquetas()      

    except Exception as e:
        print(f'Error: {e}')

else:
    print('Saliendo del programa') 