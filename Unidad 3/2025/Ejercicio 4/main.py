from clasegestorplanes import GestorPlanes

def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Dada una posición de la lista: Mostrar por pantalla qué tipo de plan se encuentra almacenado en dicha posición (usar la función isinstance()).
                        2) Leer por teclado una cobertura geográfica y contar y mostrar la cantidad de planes que corresponden a la misma.
                        3) Ingresar por teclado una cantidad de canales internacionales y mostrar el /los nombres de las compañías que ofrecen una cantidad mayor o igual a la ingresada.
                        4) Para todos los planes en la lista, mostrar: Tipo de plan, nombre de la compañía, duración del plan, cobertura geográfica e importe final. Este ítem debe resolverlo en la clase base.
                        5)Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestor = GestorPlanes()
    gestor.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            posicion = int(input("Ingrese la posicion que quiere saber empieza en 0"))
            gestor.mostratipo(posicion)
        elif opcion == 2:
            try:
                cobertura = input("Ingrese la cobertura geografica que quiere saber, puede ser Nacional, Nacional e Internacional o Regional").lower()
                gestor.contarplanes(cobertura)
            except ValueError as e:
                print(e)
        elif opcion == 3:
            try:
                cantidad = int(input("Ingrese una cantidad de canales: "))
                gestor.mostrarcompania(cantidad)
            except ValueError:
                print("Debe ingresar un número entero válido.")
            
        elif opcion == 4:
            gestor.mostrar4()
        elif opcion == 5:
            gestor.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")