class Fechadefutbol:
    __fechadelpartido:int
    __iddellocal:int
    __iddelvisitante:int
    __cantidadgoleslocal:int
    __cantidadgolesvisitante:int
    
    def __init__(self, fechadelpartido, iddellocal, iddelvisitante, cantidadgoleslocal, cantidadgolesvisitante):
        self.__fechadelpartido = fechadelpartido
        self.__iddellocal = iddellocal
        self.__iddelvisitante = iddelvisitante
        self.__cantidadgoleslocal = cantidadgoleslocal
        self.__cantidadgolesvisitante = cantidadgolesvisitante

    def __str__(self):
        return f'Fecha del partido: {self.__fechadelpartido}, ID del local: {self.__iddellocal}, ID del visitante: {self.__iddelvisitante}, Goles del local: {self.__cantidadgoleslocal}, Goles del visitante: {self.__cantidadgolesvisitante}'

    def getfechadelpartido(self):
        return self.__fechadelpartido

    def getiddellocal(self):
        return self.__iddellocal

    def getiddelvisitante(self):
        return self.__iddelvisitante

    def getcantidadgoleslocal(self):
        return self.__cantidadgoleslocal

    def getcantidadgolesvisitante(self):
        return self.__cantidadgolesvisitante