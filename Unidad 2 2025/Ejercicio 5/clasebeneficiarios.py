class Beneficiarios:
    __dni:int
    __nombre:str
    __apellido:str
    __carrera:str
    __facultad:str
    __añoquecursa:int
    __promedio:int
    __idbeca:int
    
    def __init__(self, dni:int, nombre:str, apellido:str, carrera:str, facultad:str, añoquecursa:int, promedio:int, idbeca:int):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__añoquecursa = añoquecursa
        self.__promedio = promedio
        self.__idbeca = idbeca
    
    def __str__(self):
        return f"DNI: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Carrera: {self.__carrera}, Facultad: {self.__facultad}, Año que cursa: {self.__añoquecursa}, Promedio: {self.__promedio}, ID Beca: {self.__idbeca}"
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getCarrera(self):
        return self.__carrera
    
    def getFacultad(self):
        return self.__facultad
    
    def getAñoQueCursa(self):
        return self.__añoquecursa
    
    def getPromedio(self):
        return self.__promedio
    
    def getIdBeca(self):
        return self.__idbeca
    
    def __gt__(self, otro):
        if isinstance(otro, Beneficiarios):
            return self.__facultad > otro.getFacultad()