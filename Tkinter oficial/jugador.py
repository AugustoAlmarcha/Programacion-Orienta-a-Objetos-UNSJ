class Jugador:
    __nombre:int
    __puntaje:int
    __fecha:str
    __hora:str
    def __init__(self, nombre, puntaje, fecha, hora):
        self.__nombre = nombre
        self.__puntaje = puntaje
        self.__fecha = fecha
        self.__hora = hora
    
    def getNombre(self):
        return self.__nombre
    
    def getPuntaje(self):
        return self.__puntaje
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora    
    
    def __gt__(self, otro):
        return self.__puntaje > otro.getPuntaje()
    
    def __str__(self):
        return f"Jugador: {self.__nombre}, Puntaje: {self.__puntaje}, Fecha: {self.__fecha}, Hora: {self.__hora}"