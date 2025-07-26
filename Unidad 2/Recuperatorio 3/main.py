from gestorcabanas import *
from gestoreservas import *

def main():
    opcion=None
    try:
        opcion=int(input("""        Menu de opciones
                        1)Ingresar por teclado una cantidad de huéspedes y mostrar el o los números de las cabañas
                        que tienen una capacidad igual o mayor a la cantidad ingresada y no tienen ninguna reserva
                        registrada.
                        
                        2)Ingresar una fecha y emitir un listado con las reservas cuya fecha de inicio del hospedaje sea
                        igual a la ingresada. El listado debe tener el siguiente formato:

                        3)Mostrar Todo
                        
                        0)Salir
                        """))
    except ValueError:
        pass
    return opcion

if __name__ == '__main__':
    gestorreservas=GestorReservas()
    gestorcabanas=GestorCabanas()
    gestorreservas.cargarcsv()
    gestorcabanas.cargarcsv()
    opcion=main()
    while opcion != 0:
        if opcion == 1:
            gestorcabanas.buscarCabana(gestorreservas)
        elif opcion == 2:
            gestorreservas.reservas(gestorcabanas)
        elif opcion == 3:
            gestorcabanas.mostrar()
            gestorreservas.mostrar()
        else:
            print('Opcion incorrecta')
        opcion=main()
    print('Fin del programa')
    
    