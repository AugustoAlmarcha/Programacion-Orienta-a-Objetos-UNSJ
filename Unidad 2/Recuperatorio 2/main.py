from clasegestormiembro import *
from clasegestorvisualizaciones import *

def menu():
    opcion=None
    try:
        opcion=int(input("""         Menu
                        1) Ingresar el correo electrónico de un miembro e indicar la cantidad total de minutos que ha
                        visto películas.
                            
                        2)Mostrar apellido, nombre y correo electrónico de las miembros que han realizado
                        visualizaciones simultáneas. Es decir, para el mismo miembro, en la misma fecha y a la misma
                        hora hay registradas más de una visualización.
                        
                        3) Mostrar Todo
                        
                        0) Salir
                        """))
    except ValueError:
        pass
    return opcion

if __name__ == '__main__':
    gm=GestorMiembro()
    gm.cargarcsv()
    gv=GestorVisualizaciones()
    gv.cargarcsv()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            gv.cantidadtotalminutos(gm)
        elif opcion==2:
            gv.visualizacionsimultanea(gm)
        elif opcion==3:
            gm.mostrar()
            gv.mostrar()
        else:
            print("Opción no válida")
        opcion=menu()
    print("Fin del programa")
