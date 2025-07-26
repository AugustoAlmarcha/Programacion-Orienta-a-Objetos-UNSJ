from claselistapublicaciones import Lista
from claselibro import Libro
from claseCD import CD

def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Agregar publicaciones a la colección
                        2) Dada una posición de la lista: Mostrar por pantalla qué tipo de publicación se
encuentra almacenada en dicha posición (usar la función isinstance()).
                        3) Mostrar la cantidad de publicaciones de cada tipo.
                        4) Recorrer la colección y mostrar para todas las publicaciones Titulo, categoría e
importe de venta.
                        5)Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    lista = Lista()
    lista.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            opcionx= input("Que tipo de publicación desea agregar? (Libro/CD): ").strip().lower()
            if opcionx == "libro":
                titulo = input("Ingrese el título del libro: ")
                categoria = input("Ingrese la categoría del libro: ")
                precio = float(input("Ingrese el precio del libro: "))
                nombreAutor = input("Ingrese el nombre del autor: ")
                fechaPublicacion = input("Ingrese la fecha de publicación (dd/mm/yyyy): ")
                cantidadPaginas = int(input("Ingrese la cantidad de páginas: "))
                lista.agregar(Libro(titulo, categoria, precio, nombreAutor, fechaPublicacion, cantidadPaginas))
            elif opcionx == "cd":
                titulo = input("Ingrese el título del CD: ")
                categoria = input("Ingrese la categoría del CD: ")
                precio = float(input("Ingrese el precio del CD: "))
                tiempoProduccionMinutos = int(input("Ingrese el tiempo de producción en minutos: "))
                nombreNarrador = input("Ingrese el nombre del narrador: ")
                lista.agregar(CD(titulo, categoria, precio, tiempoProduccionMinutos, nombreNarrador))
            else:
                print("Tipo de publicación no reconocida.")
        elif opcion == 2:
            posicion=int(input("Ingrese la posición de la publicación que desea verificar: "))
            lista.buscarpublicacion(posicion)
        elif opcion == 3:
            lista.cantidadPublicaciones()
        elif opcion == 4:
            lista.recorrer()
        elif opcion == 5:
            lista.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")