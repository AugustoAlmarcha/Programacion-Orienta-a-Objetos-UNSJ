from manejadordepartamentos import *
from claseaccidente import *

def menu():
    op=None
    try:
        op=int(input("""
                            Menú de Opciones
            [6] Ingrese accidentes
            [1] Dado un numero de mes, mostrar para cada uno de los Departamentosnombre del departamento y el total de accidentes ocurridos en el mes dado. .
            [2] Dado un mes, mostrar nombre de departamento y cantidad de accidentes, para el departamento que tuvo la mayor cantidad de accidentes. 
            [3] Dado el nombre de un departamento indicar la cantidad total de accidentes ocurridos el año anterior. 
            [5] Mostrar los datos registrados con el siguiente formato. La fila “TOTAL” se debe mostrar el total de accidentes del mes. 
            [7] Mostrar accidentes
            [8]
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    opcion=menu()
    depas=ManejadorDepartamentos()
    depas.cargarcsv()
    depas.mostrardepartamentos()
    accidentes=Accidente()
    while opcion!=0:
        if opcion==1:
            depas.mostraraccidenteespecifico(accidentes)
        elif opcion==2:
            depas.maximoaccidente(accidentes)
        elif opcion==3:
            depas.totalaccidentesdepa(accidentes)
        elif opcion==6:
            accidentes.agregar_accidente()
        elif opcion==7:
            accidentes.mostrar_accidentes()
        elif opcion==8:
            accidentes.mostrar_accidentes_ordenados()
        opcion=menu()