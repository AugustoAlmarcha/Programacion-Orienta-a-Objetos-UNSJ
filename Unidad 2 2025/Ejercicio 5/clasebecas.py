class Becas:
    __idbeca:int
    __tipobeca:str
    __importe:float
    
    def __init__(self, idbeca:int, tipobeca:str, importe:float):
        self.__idbeca = idbeca
        self.__tipobeca = tipobeca
        self.__importe = importe
        
    def __str__(self):
        return f"ID Beca: {self.__idbeca}, Tipo de Beca: {self.__tipobeca}, Importe: {self.__importe}"
    
    def getIdBeca(self):
        return self.__idbeca
    
    def getTipoBeca(self):
        return self.__tipobeca
    
    def getImporte(self):
        return self.__importe
    
    