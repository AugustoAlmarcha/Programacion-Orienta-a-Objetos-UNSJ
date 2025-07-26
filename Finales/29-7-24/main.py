from gestorclientes import *
def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Insertar objetos al final de la colección.
                        2) Para cada cliente Nacional que se encuentre en la colección, mostrar Nombre del
cliente y el nombre de la provincia.
                        3) Dada una posición ingresada por teclado, indicar que tipo de cliente se encuentra
en esa posición.
                        4)Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    lista = ListaClientes()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            opcionx= input("Que tipo de cliente desea agregar? (Nacional/Local): ").strip().lower()
            if opcionx == "local":
                nombre = input("Ingrese el nombre del cliente: ").strip().capitalize()
                apellido= input("Ingrese el apellido del cliente: ").strip().capitalize()
                email= input("Ingrese el correo del cliente: ").strip()
                contraseña=input("Ingrese la contraseña del cliente: ").strip()
                direccionpostal= input("Ingrese la direccion del cliente: ").strip().capitalize()
                telefono= input("Ingrese el telefono del cliente: ").strip()
                lista.agregaralfinal(ClientesLocales(nombre,apellido,email,contraseña,direccionpostal,telefono))
            elif opcionx == "nacional":
                nombre = input("Ingrese el nombre del cliente: ").strip().capitalize()
                apellido= input("Ingrese el apellido del cliente: ").strip().capitalize()
                email= input("Ingrese el correo del cliente: ").strip()
                contraseña=input("Ingrese la contraseña del cliente: ").strip()
                direccionpostal= input("Ingrese la direccion del cliente: ").strip().capitalize()
                telefono= input("Ingrese el telefono del cliente: ").strip()
                provincia = input("Ingrese la provincia del cliente: ").strip().capitalize()
                localidad = input("Ingrese la localidad").strip().capitalize()
                codigopostal= input("Ingrese el codigo postal del cliente: ").strip()
                lista.agregaralfinal(clientesNacionales(nombre,apellido,email,contraseña,direccionpostal,telefono,provincia,localidad,codigopostal))
            else:
                print("Tipo de cliente no reconocido.")
        elif opcion == 2:
            lista.esclientenacional()
        elif opcion == 3:
            posicion = int(input("Ingrese la posicion que busca: "))
            lista.clienteenposicion(posicion)
        elif opcion == 4:
            lista.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")