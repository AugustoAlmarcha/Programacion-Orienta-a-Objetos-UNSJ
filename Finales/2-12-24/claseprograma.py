from datetime import datetime
class Programa:
    __nombre:str
    __horainicio:datetime
    __horafin:datetime
    
    def __init__(self,nombre,inicio,fin):
        self.__nombre = nombre
        self.__horainicio = inicio
        self.__horafin = fin
        
    def getNombre(self):
        return self.__nombre
    
    def getHorainicio(self):
        return self.__horainicio
    
    def getHorafin(self):
        return self.__horafin
    
    def __str__(self):
        return (f"Nombre: {self.__nombre}, Hora inicio: {self.__horainicio}, Hora fin:{self.__horafin}")