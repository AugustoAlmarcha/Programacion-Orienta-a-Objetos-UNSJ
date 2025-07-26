from claselibro import Libro
from clasebiblioteca import Biblioteca
import csv

class GestorBiblioteca:
    __listabibliotecas:list
    __listalibros:list
    
    def __init__(self):
        self.__listabibliotecas = []
        self.__listalibros = []
        
    def agregar_biblioteca(self, biblioteca:Biblioteca):
        self.__listabibliotecas.append(biblioteca)
        
    def agregar_libro(self, libro:Libro):
        self.__listalibros.append(libro)
        
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 3\2025\Ejercicio 2\Biblioteca.csv")
            reader = csv.reader(archivo, delimiter=';')
            for fila in reader:
                if len(fila) == 3:
                    bibliotecax= Biblioteca(fila[0], fila[1], fila[2])
                    self.agregar_biblioteca(bibliotecax)
                elif len(fila) == 4:
                    libro= Libro(fila[0], fila[1], fila[2], fila[3])
                    self.agregar_libro(libro)
                    bibliotecax.agregar_libro(libro)
        except Exception as e:
            print("Error al cargar el archivo CSV:", e)
        finally:
            archivo.close()
            
    def mostrar(self):
        for biblioteca in self.__listabibliotecas:
            print(biblioteca)
            
        for libro in self.__listalibros:
            print("------------Libros Sueltos--------------")
            print(libro)
    
    def agregarlibroabiblioteca(self,titulo,biblioteca):
        i=0
        band=False
        bibliotecaencontrada=False
        while i < len(self.__listalibros) and not band:
            if self.__listalibros[i].get_titulo() == titulo:
                band = True
                if band is True:
                    for bibliotecax in self.__listabibliotecas:
                        if bibliotecax.get_nombre().lower() == biblioteca:
                            print("Se encontro la biblioteca")
                            bibliotecaencontrada=True
                            bibliotecax.agregarnuevolibro(self.__listalibros[i])        
            i += 1
        if not band:
            print("El titulo del libro no existe")
        elif bibliotecaencontrada is False and band is True:
                print("No se encontro la biblioteca")
    
    def eliminarlibro(self,biblioteca,libro):
        i=0
        band=False
        while i < len(self.__listabibliotecas) and band is False:
            if self.__listabibliotecas[i].get_nombre() == biblioteca:
                self.__listabibliotecas[i].eliminar(libro)
                band=True
            i+=1
        if band is False:
            print("No se encontro la biblioteca")
            
    def buscarbiblioteca(self,titulo):
        i=0
        band=False
        while i < len(self.__listabibliotecas) and band is False:
            libro=self.__listabibliotecas[i].buscar(titulo)
            if libro is not None:
                print(f"Se encontro el libro {titulo} en la biblioteca {self.__listabibliotecas[i].get_nombre()}, es un libro cuyo genero es {libro.get_genero()} y su autor es {libro.get_autor()}")
                band=True
            i+=1
            
    def mostrarlibrosporbiblioteca(self):
        i=0
        while i<len(self.__listabibliotecas):
            print(f"En la biblioteca {self.__listabibliotecas[i].get_nombre()} se encuentran los siguientes libros: ")
            self.__listabibliotecas[i].listar()
            i+=1

# if __name__ == "__main__":
#     gestor = GestorBiblioteca()
#     gestor.cargarcsv()
#     gestor.mostrar()