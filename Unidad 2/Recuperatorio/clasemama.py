class Mama:
    __dni:str
    __edad:int
    __Nya:str
    
    def __init__(self,dni,edad,Nya):
        self.__dni=dni
        self.__edad=edad
        self.__Nya=Nya
        
    def getDni(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    def getNya(self):
        return self.__Nya
    
    def __str__(self):
        return f'La paciente cuyo nombre es {self.__Nya} con DNI: {self.__dni} y edad: {self.__edad}'
    