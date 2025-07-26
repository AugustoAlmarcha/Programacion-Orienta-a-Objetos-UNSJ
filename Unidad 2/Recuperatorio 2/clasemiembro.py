class Miembro:
    __id:int
    __nya:str
    __correo:str
    
    def __init__(self, id:int, nya:str, correo:str):
        self.__id = id
        self.__nya = nya
        self.__correo = correo
        
    def getID(self):
        return self.__id
    
    def getNya(self):
        return self.__nya
    
    def getCorreo(self):
        return self.__correo
    
    def __str__(self):
        return f'{self.__id} - {self.__nya} - {self.__correo}'