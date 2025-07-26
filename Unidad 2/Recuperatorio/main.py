from gestormamas import *
from gestornacimientos import *

def main():
    opcion=None
    try:
        opcion=int(input("""                        Menu de opciones
                        1: Ingresar por teclado el DNI de una mamá, mostrar la siguiente información
                        2:Mostrar los datos de la/s mamá/s que han tenido parto múltiple (mellizos, gemelos, trillizos,
                        etc). Es decir, para una misma mamá en una misma fecha se registró más de un nacimiento.
                        3:Mostrar Todo
                        0:Salir
                         
                        """))
    except ValueError:
        pass
    return opcion

if __name__=="__main__":
    gestormamas=GestorMamas()
    gestornacimientos=GestorNacimientos()
    gestormamas.cargarcsv()
    gestornacimientos.cargarcsv()
    opcion=main()
    while opcion!=0:
        if opcion==1:
            dni=input("Ingrese el DNI de la mama: ")
            gestormamas.mostrardatosmamas(dni,gestornacimientos)
        elif opcion==2:
            gestornacimientos.partosmultiples(gestormamas)
        elif opcion==3:
            gestornacimientos.mostrar()
            gestormamas.mostrar()
        else:
            print("Opcion incorrecta")
        opcion=main()

