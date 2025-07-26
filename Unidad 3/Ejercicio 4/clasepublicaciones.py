from abc import ABC
import abc
class Publicaciones(ABC):
    __titulo:str
    __categoria:str
    __precio:float
    
    def __init__(self,titulo,categoria,precio):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio = precio
        
    def getTitulo(self):
        return self.__titulo
    
    def getCategoria(self):
        return self.__categoria
    
    def getPrecio(self):
        return self.__precio
    
    def __str__(self):
        return f"Titulo: {self.__titulo}, Categoria: {self.__categoria}, Precio: {self.__precio}"
    
    @abc.abstractmethod
    def calcularPrecio(self):
        pass