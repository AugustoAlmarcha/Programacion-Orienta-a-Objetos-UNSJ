from clasepublicaciones import Publicaciones
from datetime import datetime
class Libro(Publicaciones):
    __nombreAutor:str
    __fechapublicacion:str
    __cantidadPaginas:int
    
    def __init__(self, titulo,categoria,precio, nombreAutor, fechapublicacion, cantidadPaginas):
        super().__init__(titulo, categoria, precio)
        self.__nombreAutor = nombreAutor
        self.__fechapublicacion = fechapublicacion
        self.__cantidadPaginas = cantidadPaginas

    def getNombreAutor(self):
        return self.__nombreAutor

    def getFechaPublicacion(self):
        return self.__fechapublicacion

    def getCantidadPaginas(self):
        return self.__cantidadPaginas

    def __str__(self):
        return super().__str__() + f", Autor: {self.__nombreAutor}, Fecha de Publicacion: {self.__fechapublicacion}, Cantidad de Paginas: {self.__cantidadPaginas}, Precio Final: {self.calcularPrecio()}"

    def calcularPrecio(self):
        fecha = datetime.strptime(self.__fechapublicacion, "%d/%m/%Y")
        if fecha.year == datetime.now().year:
            return self.getPrecio()
        else:
            añosdiferencia = datetime.now().year - fecha.year
            precio_final = self.getPrecio() - añosdiferencia * 0.01 * self.getPrecio()
            return precio_final