from gestormedios import *
def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Agregar medios de comunicación a la instancia de la clase de control definida antes.
                        2) Leer por teclado el nombre de un programa de radio y muestre el nombre del medio de
comunicación, la frecuencia y el horario de inicio de transmisión. El método que resuelve este
requerimiento debe lanzar una excepción (Excep􀆟on) en caso de no encontrar el nombre
ingresado.
                        3) Indicar para cada medio de comunicación el nombre, la audiencia es􀆟mada y el índice de
audiencia.
                        4) Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestor = GestorMedios()
    gestor.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            medio = input("Ingrese el medio que desea agregar (Radio o Prensa Escrita)").lower()
            if medio == "radio" or medio == "prensa escrita":
                nombre= input("Ingrese el nombre del nuevo medio")
                audiencia= int(input("Ingrese la audiencia estimada"))
                if medio== "radio":
                    frecuencia = input("Ingrese la frecuencia del medio")
                    gestor.agregarMedio(Radio(nombre,audiencia,frecuencia))
                elif medio =="prensa escrita":
                    while True:
                        periodicidad=input("Ingrese la periodicidad mensual o semanal").lower()
                        if periodicidad == "mensual" or periodicidad == "semanal":
                            break
                        else:
                            print("Periodicidad no válida")
                    cantsecciones = int(input("Ingrese la cantidad de secciones"))
                    gestor.agregarMedio(PrensaEscrita(nombre,audiencia,periodicidad,cantsecciones))
            else:
                print("Medio no válido")
        elif opcion == 2:
            nombre = input("Ingrese el nombre del programa de radio que desea buscar").strip()
            try:
                gestor.buscarPrograma(nombre)
            except ValueError:
                print("No se encontró el programa de radio")
        elif opcion == 3:
            gestor.mostrarMediosespecificos()
        elif opcion == 4:
            gestor.mostrarMedios()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")