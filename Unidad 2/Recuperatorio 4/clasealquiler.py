class Alquiler:
    __nombreInquilino:str
    __idcancha:str
    __hora:str
    __minutos:str
    __duracion:int
    
    def __init__(self,nombreInquilino:str,idcancha:str,hora:int,minutos:int,duracion:int):
        self.__nombreInquilino=nombreInquilino
        self.__idcancha=idcancha
        self.__hora=hora
        self.__minutos=minutos
        self.__duracion=duracion
        
    def getnombreInquilino(self):
        return self.__nombreInquilino
    
    def getidcancha(self):
        return self.__idcancha
    
    def gethora(self):
        return self.__hora
    
    def getminutos(self):
        return self.__minutos
    
    def getduracion(self):
        return self.__duracion
    
    def __str__(self):
        return f'{self.__nombreInquilino} - {self.__idcancha} - {self.__hora}:{self.__minutos} - {self.__duracion}hs'
    
    def __gt__(self,otro):
        if self.__hora==otro.gethora():
            return self.__minutos>otro.getminutos()
        else:
            return self.__hora>otro.gethora()
        
    