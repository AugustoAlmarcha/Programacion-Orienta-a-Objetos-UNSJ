class Bateria:
    __patente:str
    __marca="CATL"
    __capacidadcarga:int
    __cargaactual:int

    def __init__(self,patente,capacidadcarga,cargaactual):
        self.__patente= patente
        self.__capacidadcarga= capacidadcarga
        self.__cargaactual= cargaactual

    def getpatente(self):
        return self.__patente

    def getcapacidadcarga(self):
        return self.__capacidadcarga
    
    def getcargaactual(self):
        return self.__cargaactual
    
    @classmethod
    def getmarca(cls):
        return cls.__marca
    
    def energiadisponible(self):
        return (self.__capacidadcarga - self.__cargaactual) / 10 
    
    def __str__(self):
        return f"Patente: {self.__patente}, Marca: {self.getmarca()}, Capacidad de carga: {self.__capacidadcarga}, Carga actual: {self.__cargaactual}"