from manejadorcarrera import *
from manejadordefacultad import *

def main():
    opcion=None
    try:
        opcion=int(input("""        Menu de Opciones
                        1) Cargar los datos de las Carreras desde el archivo Carreras.csv.
                        
                        2)Cargar los datos de las Facultades desde del archivo Facultades.csv.
                        
                        3)Dado el Nombre de una Carrera, mostrar el nombre de la Facultad en la que se dicta.
                        
                        4)Para todas las facultades calcular y mostrar la cantidad de carreras que se dictan en
                        cada una de ellas.
                        
                        5)Dado el nombre de una Facultad, generar un listado ordenado alfabéticamente, que
                        muestre: nombre y duración de de las carreras que en ella se dictan. Para ello, el
                        analista le solicita que en la clase que representa a las carreras, sobrecargue el
                        operador __lt__.
                        
                        6)Mostrar Todo
                        
                        7)Ordenar
                        
                        0) Salir
                        
                        
                
                        """))
    except ValueError:
        pass
    return opcion

if __name__=="__main__":
    gestorcarrera=ManejadorCarrera()
    gestorfacultad=Manejadorfacultad()
    opcion=main()
    while opcion!=0:
        if opcion==1:
            gestorcarrera.cargarcsv()
        elif opcion==2:
            gestorfacultad.cargarcsv()
        elif opcion==3:
            gestorcarrera.quefacultad(gestorfacultad)
        elif opcion==4:
            gestorcarrera.cantidadcarrerasx(gestorfacultad)
        elif opcion==5:
            gestorfacultad.buscarfacultadxnombre(gestorcarrera)
        elif opcion==6:
            print("----Universidades-----\n")
            gestorfacultad.mostrar()
            print("\n----Carreras-----\n")
            gestorcarrera.mostrarcarreras()
        elif opcion==7:
            gestorcarrera.ordenar()
        else:
            print('Opcion incorrecta')
        opcion=main()
    print('Fin del programa')