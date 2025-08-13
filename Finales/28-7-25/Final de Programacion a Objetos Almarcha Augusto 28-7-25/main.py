from gestorvehiculos import *

def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Leer desde el archivo “Vehículos.csv”, los datos de los distintos tipos de vehículo, y 
                            agregarlos al principio de la lista que implementa el Gestor el primer carácter de cada fila, 
                            distingue el tipo de vehículo (‘C’-Colectivo, ‘E’-Eléctrico). Los datos de las baterías, vienen en 
                            un archivo denominado “Baterias.csv”. Agregar las baterías a los vehículos eléctricos que 
                            correspondan (misma patente). Ambos archivos tienen como separador “;”. 
                        2) Leer por teclado una distancia en km, listar la patente de los vehículos eléctricos que pueden 
realizar el recorrido con la energía disponible de todas las baterías. 
                        3) Mostrar para todos los vehículos: patente, cantidad de pasajeros, tipo de vehículo y el 
consumo para recorrer. 
                        4) Leer por teclado los datos de un nuevo vehículo colectivo, y una posición de la lista, si la 
posición existe (mayor que 0, cabeza la lista, y menor que la cantidad de elementos de la 
lista), se agrega en la posición indicada, en caso de que la posición no exista se debe lanzar la 
excepción IndexError en el método del Gestor de Vehículos. Esta excepción debe controlarla 
en el programa principal. 
                        5)Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestorvehiculos = ListaVehiculos()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            gestorvehiculos.cargarcsv()
        elif opcion == 2:
            distanciax = int(input("Ingrese la distancia en km: "))
            try:
                gestorvehiculos.listarvehiculoselectricos(distanciax)
            except Exception as e:
                print("Error: ", e)
        elif opcion == 3:
            try:
                gestorvehiculos.mostrarespecifico()
            except Exception as e:
                print("Error: ", e)
        elif opcion == 4:
            try:
                colectivox= Colectivo(
                    input("Ingrese patente: "),
                    int(input("Ingrese capacidad de pasajeros: ")),
                    float(input("Ingrese kilometros a recorrer: ")),
                    input("Ingrese nombre de la empresa: "),
                    int(input("Ingrese capacidad de combustible: ")),
                    input("Ingrese tipo de combustible (gasoil o gnc): ").lower()
                )
                posicion = int(input("Ingrese la posición donde desea agregar el colectivo: "))
                gestorvehiculos.agregarx(colectivox, posicion)
            except IndexError as e:
                print("Error: ", e)
        elif opcion == 5:
            gestorvehiculos.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")