class Nacimiento:
    __dni:str
    __tipoparto:str
    __fecha:str
    __hora:str
    __peso:float
    __altura:int
    
    def __init__ (self,dni,tipoparto,fecha,hora,peso,altura):
        self.__dni=dni
        self.__tipoparto=tipoparto
        self.__fecha=fecha
        self.__hora=hora
        self.__peso=peso
        self.__altura=altura
        
    def getDni(self):
        return self.__dni
    
    def getTipoParto(self):
        return self.__tipoparto
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura
    
    def __str__(self):
        return f'El paciente nacido cuya madre tiene DNI: {self.__dni}, nacio por parto {self.__tipoparto} (N natural, C cecarea), nacio el dia {self.__fecha} a las {self.__hora} con un peso de {self.__peso} y una altura de {self.__altura}'
    
    def __eq__(self,otro):
        return self.__dni==otro.__dni and self.__fecha==otro.__fecha
    