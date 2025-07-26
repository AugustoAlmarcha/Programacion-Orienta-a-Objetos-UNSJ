from clasegestoredificio import *
def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Dado el nombre de un edificio mostrar: Nombre y apellido de los propietarios de
cada uno de los departamentos del edificio.
                        2) Mostrar la superficie total cubierta de un edificio.
                        3) Dado el nombre de un propietario, mostrar la superficie total cubierta de su
departamento e indicar que porcentaje representa del total de la superficie
cubierta del edificio.
                        4) Dado un número de piso: contar y mostrar la cantidad de departamentos que
tienen 3 dormitorios y más de un baño.
                        5) Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestor = GestorEdificio()
    gestor.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            nombre = input("Ingrese el nombre del edificio: ")
            gestor.mostrarpropietarios(nombre)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del edificio: ")
            gestor.superficietotalx(nombre)
        elif opcion == 3:
            nombrepropietario = input("Ingrese el nombre del propietario: ")
            gestor.superficie(nombrepropietario)
        elif opcion == 4:
            numero=int(input("Ingrese el numero de piso: "))
            gestor.contar(numero)
        elif opcion == 5:
            gestor.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")