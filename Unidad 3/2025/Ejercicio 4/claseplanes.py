from abc import ABC
import abc

class Planes(ABC):
    __nombrecompañia:str
    __duracion:int
    __cobertura:str
    __preciobase:float
    
    def __init__(self, nombre,duracion,cobertura,precio):
        self.__nombrecompañia=nombre
        self.__duracion=duracion
        self.__cobertura=cobertura
        self.__preciobase=precio
        
    def getnombre(self):
        return self.__nombrecompañia
    
    def getduracion(self):
        return self.__duracion
    
    def getcobertura(self):
        return self.__cobertura
    
    def getpreciobase(self):
        return self.__preciobase
    
    def calcularprecio(self):
        modificador = self.obtenermodificador()
        return self.__preciobase * (1 + modificador)
    
    @abc.abstractmethod
    def obtenermodificador(self):
        pass
        
    def __str__(self):
        return f"Nombre de la compañia: {self.__nombrecompañia}, Duración: {self.__duracion} días, Cobertura: {self.__cobertura}, Precio base: {self.__preciobase}"
    
    def mostrarresumen(self):
        print(f"Tipo de plan: {type(self).__name__}")
        print(f"Nombre de la compañía: {self.__nombrecompañia}")
        print(f"Duración del plan: {self.__duracion} días")
        print(f"Cobertura geográfica: {self.__cobertura}")
        print(f"Importe final: ${self.calcularprecio():.2f}")
        print("-" * 40)
    
