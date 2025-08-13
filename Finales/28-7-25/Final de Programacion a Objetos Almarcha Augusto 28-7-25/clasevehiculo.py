from abc import ABC, abstractmethod
class Vehiculo(ABC):
    __patente:str
    __capacidadpasajeros:int
    __kilometrosarecorrer:float

    def __init__(self,patente,capacidad,km):
        self.__patente= patente
        self.__capacidadpasajeros= capacidad
        self.__kilometrosarecorrer= km

    def getpatente(self):
        return self.__patente
    
    def getcapacidad(self):
        return self.__capacidadpasajeros
    
    def getkm(self):
        return self.__kilometrosarecorrer
    
    def __str__(self):
        return f"Patente: {self.__patente}, Capacidad: {self.__capacidadpasajeros}, Kilometros a recorrer: {self.__kilometrosarecorrer}"
    
    def consumo(self):
        return self.__kilometrosarecorrer  * self.calculo()
    
    @abstractmethod
    def calculo(self):
        pass