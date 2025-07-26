from clasemedio import Medio

class PrensaEscrita(Medio):
    __periodicidad:str
    __cantsecciones:int
    
    def __init__(self,nombre,audiencia,periodicidad,cantsecciones):
        super().__init__(nombre,audiencia)
        self.__periodicidad = periodicidad
        self.__cantsecciones = cantsecciones
        
    def get_periodicidad(self):
        return self.__periodicidad
    
    def get_cantsecciones(self):
        return self.__cantsecciones
    
    def __str__(self):
        return super().__str__() + (f"Periodicidad {self.__periodicidad}, Cantidad de Secciones: {self.__cantsecciones}")
    
    def calculo(self):
        if self.__periodicidad.lower().strip() == "mensual":
            return self.__cantsecciones
        elif self.__periodicidad.lower().strip() == "semanal":
            return self.__cantsecciones * 4