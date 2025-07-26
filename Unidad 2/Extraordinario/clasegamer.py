class Gamer:
    __idJugador:int
    __dni:int
    __nombre:str
    __apellidos:str
    __alias:str
    __plan:str
    __importebase:int
    __tiempolimite:int
    
    def __init__(self,idJugador:int,dni:int,nombre:str,apellidos:str,alias:str,plan:str,importebase:int,tiempolimite:int):
        self.__idJugador = idJugador
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__alias = alias
        self.__plan = plan
        self.__importebase = importebase
        self.__tiempolimite = tiempolimite
        
    def getIdJugador(self):
        return self.__idJugador
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellidos(self):
        return self.__apellidos
    
    def getAlias(self):
        return self.__alias
    
    def getPlan(self):
        return self.__plan
    
    def getImporteBase(self):
        return self.__importebase
    
    def getTiempoLimite(self):
        return self.__tiempolimite
    
    def __str__(self):
        return f'{self.__idJugador} {self.__dni} {self.__nombre} {self.__apellidos} {self.__alias} {self.__plan} {self.__importebase} {self.__tiempolimite}'