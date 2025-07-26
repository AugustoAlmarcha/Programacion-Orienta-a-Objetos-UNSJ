from gestordealquileres import *
from gestordecanchas import *

def menu():
    opcion=None
    try:
        opcion=int(input(""" Menu de Opciones
                        1: Emitir un listado ordenado por hora y minutos con todos los alquileres registrados y con el
                        siguiente formato:

                        2:Ingresar el identificador de una cancha y mostrar la cantidad total de minutos que estuvo
                        alquilada.
                        
                        3:Mostrar Todo
                        
                        0: Salir
                    
                        """))
    except ValueError:
        pass
    return opcion

if __name__ == "__main__":
    gestorCanchas=Gestorcanchas()
    gestorCanchas.cargarcsv()
    gestorAlquileres=GestorAlquileres()
    gestorAlquileres.cargarcsv()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            gestorAlquileres.ordenar()
            gestorAlquileres.formato(gestorCanchas)
        elif opcion==2:
            gestorAlquileres.totalminutos()
        elif opcion==3:
            gestorCanchas.mostrar()
            gestorAlquileres.mostrar()
        else:
            print('Opcion incorrecta')
        opcion=menu()
    print('Fin del programa')
