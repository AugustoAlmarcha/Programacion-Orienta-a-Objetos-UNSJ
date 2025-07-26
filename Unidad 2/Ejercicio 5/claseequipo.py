class Equipo:
    __id:int
    __nombre:str
    __golesafavor:int
    __golesencontra:int
    __diferenciadegoles:int
    __puntos:int
    
    def __init__(self,id,nombre,goles,encontra,diferencia,puntos):
        self.__id=id
        self.__nombre=nombre
        self.__golesafavor=goles
        self.__golesencontra=encontra
        self.__diferenciadegoles=diferencia
        self.__puntos=puntos
    
    def __str__(self):
        return (f"Id: {self.__id}, Nombre: {self.__nombre}, Goles a favor: {self.__golesafavor}, Goles en contra: {self.__golesencontra}, Diferencia de goles: {self.__diferenciadegoles}, Puntos: {self.__puntos}")
    
    def getid(self):
        return self.__id

    def getnombre(self):
        return self.__nombre

    def getgolesafavor(self):
        return self.__golesafavor

    def getgolesencontra(self):
        return self.__golesencontra

    def getdiferenciadegoles(self):
        return self.__diferenciadegoles

    def getpuntos(self):
        return self.__puntos
    
    def __gt__(self,otro):
        if self.__puntos == otro.getpuntos() and self.__diferenciadegoles == otro.getdiferenciadegoles():
            return self.__golesafavor > otro.getgolesafavor()
        elif self.__puntos == otro.getpuntos():
            return self.__diferenciadegoles > otro.getdiferenciadegoles()
        else:
            return self.__puntos > otro.getpuntos()
        