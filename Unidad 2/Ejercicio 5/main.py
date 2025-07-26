from gestordeequipos import *
from gestorfechasfutbol import *

def menu():
    op=None
    try:
        op=int(input(""" 
                            Menu de opciones
                1= Leer el nombre de un equipo y obtener un listado con el siguiente formato
            
                2=Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas.
                    
                3= Ordenar la tabla de posiciones de mayor a menor
                
                4=Ordenar la tabla de posiciones de mayor a menor
                    
                5=Almacenar la tabla de posiciones ordenada en el punto anterior en un archivo .csv.
                
                6=Mostrar
                    """))
    except ValueError:
        pass
    return op

if __name__ == "__main__":
    fecha=Gestorfechas()
    equipos=GestorEquipo()
    fecha.cargarcsv()
    equipos.cargarcsv()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            print("")
        elif opcion==2:
            print("")
        elif opcion==3:
            print("")
        elif opcion==4:
            equipos.ordenar()
        elif opcion==5:
            print("Creando archivo csv.")
        elif opcion==6:
            fecha.mostrar()
            equipos.mostrarEquipos()
        opcion=menu()
    