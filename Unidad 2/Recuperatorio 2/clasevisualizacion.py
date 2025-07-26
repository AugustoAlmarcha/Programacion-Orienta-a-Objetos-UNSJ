class Visualizacion:
    __idmiembro:int
    __idpelicula:str
    __fecha:str
    __hora:str
    __minutosvistos:int
    
    def __init__(self,idmiembro:int,idpelicula:str,fecha:str,hora:str,minutos:int):
        self.__idmiembro=idmiembro
        self.__idpelicula=idpelicula
        self.__fecha=fecha
        self.__hora=hora
        self.__minutosvistos=minutos
        
    def getIDMiembro(self):
        return self.__idmiembro
    
    def getIDPelicula(self):
        return self.__idpelicula
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getMinutos(self):
        return self.__minutosvistos
    
    def __str__(self):
        return f'{self.__idmiembro} - {self.__idpelicula} - {self.__fecha} - {self.__hora} - {self.__minutosvistos}'
    
    def __eq__(self,otro):
        return self.__idmiembro==otro.getIDMiembro() and self.__fecha==otro.getFecha() and self.__hora==otro.getHora() 
    