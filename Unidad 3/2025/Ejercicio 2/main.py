from gestorbiblioteca import *
def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Agregar Libro: Permitir a la biblioteca agregar un nuevo libro a su colección.
                        2) Eliminar Libro: Permitir a la biblioteca eliminar un libro de su colección.
                        3) Para un Titulo de libro ingresado por teclado, mostrar nombre de la biblioteca en la que se encuentra, nombre del Autor y Género
                        4)  Listar Libros: Mostrar el nombre de todos los libros disponibles en la biblioteca.
                        5) Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestor = GestorBiblioteca()
    gestor.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            titulo = input("Ingrese el título del libro: ")
            biblioteca= input("Ingrese el nombre de la biblioteca a la que quiere agregar un libro: ").lower()
            gestor.agregarlibroabiblioteca(titulo,biblioteca)
        elif opcion == 2:
            biblioteca= input("Ingrese el nombre de la biblioteca que busca")
            titulo= input("Ingrese el libro que quiere eliminar")
            gestor.eliminarlibro(biblioteca,titulo)
        elif opcion == 3:
            titulo= input("Ingrese el titulo del libro que busca ").lower()
            gestor.buscarbiblioteca(titulo)
        elif opcion == 4:
            gestor.mostrarlibrosporbiblioteca()
        elif opcion == 5:
            gestor.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")