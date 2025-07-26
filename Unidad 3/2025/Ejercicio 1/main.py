from gestordehotel import GestorHotel

def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Agregar habitaciones al hotel.
                        2) Reservar una habitación.
                        3) Liberar una habitación.
                        4) Dado un tipo de habitación (sencilla, doble, suite), mostrar número y piso de las habitaciones de ese tipo.
                        5)Mostrar la cantidad de habitaciones libres por piso.
                        6) Para cada tipo de habitación mostrar el detalle asociado con el siguiente formato: 
                        Tipo_de habitacion: xxxxxxxxxx
                        Número  piso   precio por noche    disponibilidad
                        xxxxx    xx      xxx                  xxx
                        7) Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestor = GestorHotel()
    gestor.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            nombre = input("Ingrese el nombre del hotel donde quiere agregar una habitacion: ")
            gestor.agregarHabitacionx(nombre)
        elif opcion == 2:
            habitacionnumero= int(input("Ingrese el número de la habitación que desea reservar: "))
            nombre = input("Ingrese el nombre del hotel: ")
            gestor.reservarhabitacion(habitacionnumero, nombre)
        elif opcion == 3:
            habitacionnumero= int(input("Ingrese el número de la habitación que desea reservar: "))
            nombre = input("Ingrese el nombre del hotel: ")
            gestor.liberarhabitacionx(habitacionnumero, nombre)
        elif opcion == 4:
            tipo = input("Ingrese el tipo de habitación (sencilla, doble, suite): ")
            gestor.mostrarHabitacionesPorTipo(tipo)
        elif opcion == 5:
            gestor.habitacioneslibres()
        elif opcion == 6:
            gestor.mostrardetallesx()
        elif opcion == 7:
            gestor.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")