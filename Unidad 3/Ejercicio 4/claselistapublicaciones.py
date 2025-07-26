import csv
from clasenodo import Nodo
from claselibro import Libro
from claseCD import CD
class Lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def __getTope(self):
        return self.__tope
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 3\Ejercicio 4\libros.csv")
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregar(Libro(fila[0], fila[1], float(fila[2]), fila[3], fila[4], int(fila[5])))
            archivo.close()
            
            archivo2 = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 3\Ejercicio 4\cd.csv")
            reader2 = csv.reader(archivo2, delimiter=';')
            next(reader2)
            for fila in reader2:
                self.agregar(CD(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4]))
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
        
      
    def agregar(self,producto):
        nodo= Nodo(producto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        print("Cargado Exitosamente!")
    
    def mostrar(self):
        if self.__comienzo is None:
            print("No hay publicaciones para mostrar.")
        else:
            actual = self.__comienzo
            while actual is not None:
                if isinstance(actual.getDato(), Libro):
                    print("Libro:")
                elif isinstance(actual.getDato(), CD):
                    print("CD:")
                print(actual.getDato())
                actual = actual.getSiguiente()
                print("-------------------------")
    
    def buscarpublicacion(self, posicion):
        if posicion < 0 or posicion >= self.__tope:
            print("Posición inválida.")
            return
        
        actual = self.__comienzo
        for i in range(posicion):
            actual = actual.getSiguiente()
        
        if isinstance(actual.getDato(), Libro):
            print("Tipo de publicación: Libro")
        elif isinstance(actual.getDato(), CD):
            print("Tipo de publicación: CD")
        else:
            print("Tipo de publicación desconocido.")
        
        print(actual.getDato())
    
    def cantidadPublicaciones(self):
        contador_libros = 0
        contador_cd = 0
        
        actual = self.__comienzo
        while actual is not None:
            if isinstance(actual.getDato(), Libro):
                contador_libros += 1
            elif isinstance(actual.getDato(), CD):
                contador_cd += 1
            actual = actual.getSiguiente()
        
        print(f"Cantidad de Libros: {contador_libros}")
        print(f"Cantidad de CDs: {contador_cd}")
    
    def recorrer(self):
        if self.__comienzo is None:
            print("No hay publicaciones para recorrer.")
        else:
            actual = self.__comienzo
            while actual is not None:
                publicacion = actual.getDato()
                if isinstance(publicacion, Libro):
                    print("Libro:")
                elif isinstance(publicacion, CD):
                    print("CD:")
                print(f"Título: {publicacion.getTitulo()}, Categoría: {publicacion.getCategoria()}, Importe de Venta: {publicacion.calcularPrecio()}")
                actual = actual.getSiguiente()
                
# if __name__ == "__main__":
#     lista = Lista()
#     lista.cargarcsv()
#     lista.mostrar()
    
    
        