class Conexiones:
    __idJugador:int
    __direccionip:str
    __nombredeljuego:str
    __fecha:str
    __horadeinicio:int
    __horadefin:int
    
    def __init__(self,idJugador:int,direccionip:str,nombredeljuego:str,fecha:str,horadeinicio:int,horadefin:int):
        self.__idJugador = idJugador
        self.__direccionip = direccionip
        self.__nombredeljuego = nombredeljuego
        self.__fecha = fecha
        self.__horadeinicio = horadeinicio
        self.__horadefin = horadefin
        
    def getIdJugador(self):
        return self.__idJugador
    
    def getDireccionIp(self):
        return self.__direccionip
    
    def getNombreDelJuego(self):
        return self.__nombredeljuego
    
    def getFecha(self):
        return self.__fecha
    
    def getHoraDeInicio(self):
        return self.__horadeinicio
    
    def getHoraDeFin(self):
        return self.__horadefin
    
    def __str__(self):
        return f'{self.__idJugador} {self.__direccionip} {self.__nombredeljuego} {self.__fecha} {self.__horadeinicio} {self.__horadefin}'
    
    def __eq__(self, otro):
        return (self.__idJugador == otro.getIdJugador() and self.__fecha == otro.getFecha() and self.__horadeinicio == otro.getHoraDeInicio() and self.__direccionip != otro.getDireccionIp())
    
    def __lt__(self, otro):
        if self.__idJugador == otro.getIdJugador():
            return self.__fecha < otro.getFecha()
        elif self.__fecha == otro.getFecha():
            return self.__horadeinicio < otro.getHoraDeInicio()
        elif self.__horadeinicio == otro.getHoraDeInicio():
            return self.__direccionip < otro.getDireccionIp()
        else:
            return self.__idJugador < otro.getIdJugador()