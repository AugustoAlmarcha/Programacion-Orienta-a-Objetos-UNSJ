from abc import ABC
import abc
class Medio(ABC):
    __nombre:str
    __audiencia:int
    
    def __init__(self,nombre,audiencia):
        self.__nombre = nombre
        self.__audiencia = audiencia
        
    def get_nombre(self):
        return self.__nombre
    
    def get_audiencia(self):
        return self.__audiencia
    
    def __str__(self):
        return (f"Nombre: {self.__nombre}, Audiencia: {self.__audiencia} ")
    
    def indice(self):
        return self.__audiencia / self.calculo()
    
    abc.abstractmethod
    def calculo(self):
        pass