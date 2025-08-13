from clasevehiculo import Vehiculo
class Colectivo(Vehiculo):
    __nombreempresa:str
    __capacidadcombustible:int
    __tipodecombustible:str

    def __init__(self, patente, capacidad, km, nombreempresa, capacidadcombustible, tipodecombustible):
        super().__init__(patente, capacidad, km)
        self.__nombreempresa = nombreempresa
        self.__capacidadcombustible = capacidadcombustible
        self.__tipodecombustible = tipodecombustible

    def getnombreempresa(self):
        return self.__nombreempresa
    
    def getcapacidadcombustible(self):
        return self.__capacidadcombustible
    
    def gettipodecombustible(self):
        return self.__tipodecombustible
    
    def __str__(self):
        return f"{super().__str__()}, Empresa: {self.__nombreempresa}, Capacidad de combustible: {self.__capacidadcombustible}, Tipo de combustible: {self.__tipodecombustible}"
    
    def calculo(self):
        valor=0
        if self.__tipodecombustible.lower() == "gasoil":
            valor = 0.2
        elif self.__tipodecombustible.lower() == "gnc":
            valor = 0.15
        return valor
