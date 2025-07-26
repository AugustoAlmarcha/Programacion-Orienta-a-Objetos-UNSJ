from abc import ABC, abstractmethod

class Vehiculo(ABC):
    __matricula:str
    __modelo:str
    __costoxkm:float
    __cantidadedias:int
    
    def __init__(self,matricula,modelo,costoxkm,cantidadedias):
        self.__matricula=matricula
        self.__modelo=modelo
        self.__costoxkm=costoxkm
        self.__cantidadedias=cantidadedias
        
    def getMatricula(self):
        return self.__matricula
    
    def getCostoXkm(self):
        return self.__costoxkm
    
    def getmodelo(self):
        return self.__modelo
    
    def getcantidadedias(self):
        return self.__cantidadedias
    
    def __str__(self):
        return (f"Matricula {self.__matricula}, Modelo: {self.__modelo}, Costo por kilometro: {self.__costoxkm}, Cantidad de dias que lo alquilo: {self.__cantidadedias}")
    
    def alquiler(self):
        return self.__costoxkm * self.__cantidadedias + self.calculo()
    
    @abstractmethod
    def calculo(self):
        pass
        
        