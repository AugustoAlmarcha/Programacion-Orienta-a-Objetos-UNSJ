from abc import ABC 
import abc
class Paciente(ABC):
    __nombre:str
    __apellido:str
    __email:str
    __telefono:str
    valorconsulta=15000
    
    def __init__(self,nombre,apellido,email,telefono):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__telefono=telefono
        
    @classmethod
    def getvalorconsulta(cls):
        return cls.valorconsulta
    
    
    def getnombre(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido
    
    def getemail(self):
        return self.__email
    
    def gettelefono(self):
        return self.__telefono
    
    def __str__(self):
        return f'Nombre: {self.__nombre}, Apellido {self.__apellido}, Email: {self.__email}, Telefono: {self.__telefono}, Valor de la consulta: {self.getvalorconsulta()}'
    
    @abc.abstractmethod
    def calculopaciente(self):
        pass
    
    def importeacobrar(self):
        return self.getvalorconsulta() + self.calculopaciente()
    
    
    