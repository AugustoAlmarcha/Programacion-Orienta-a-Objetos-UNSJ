from clasevehiculos import Vehiculo

class Automovil(Vehiculo):
    __pasajerosmaximos:int
    __cantidadpasajerosreal:int
    
    def __init__(self,matricula,modelo,costo,dias,maximo,real):
        super().__init__(matricula,modelo,costo,dias)
        self.__pasajerosmaximos = maximo
        self.__cantidadpasajerosreal = real
        
    def __str__(self):
        return super().__str__() + (f"Cantidad de pasajeros maximo permitido {self.__pasajerosmaximos}, Pasajeros reales transportados: {self.__cantidadpasajerosreal}")
    
    def getpasajeromaximo(self):
        return self.__pasajerosmaximos
    
    def getpasajerosreales(self):
        return self.__cantidadpasajerosreal
    
    def calculo(self):
        return 5000 * self.__cantidadpasajerosreal