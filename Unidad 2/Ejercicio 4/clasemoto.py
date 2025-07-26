class Moto:
    __patente:str
    __marca:str
    __NyA:str
    __kilometraje:int
    
    def __init__(self,patente,marca,nya,kilometraje):
        self.__patente=patente
        self.__marca=marca
        self.__NyA=nya
        self.__kilometraje=kilometraje
    
    def __str__(self):
        return (f"Patente: {self.__patente}, Marca: {self.__marca}, Nombre y Apellido: {self.__NyA}, Kilometraje:{self.__kilometraje}")
    
    def getpatente(self):
        return self.__patente
    
    def getmarca(self):
        return self.__marca
    
    def getnya(self):
        return self.__NyA
    
    def getkilometraje(self):
        return self.__kilometraje
    
    
        