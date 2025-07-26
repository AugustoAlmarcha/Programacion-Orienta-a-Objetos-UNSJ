from claseplanes import Planes

class Telefonia(Planes):
    __tipodellamadas:str
    __cantidadminutos:int
    
    def __init__(self,nombre,duracion,cobertura,precio, tipo,cantidad):
        super().__init__(nombre,duracion,cobertura,precio)
        self.__tipodellamadas=tipo
        self.__cantidadminutos=cantidad
        
    def gettipodellamadas(self):
        return self.__tipodellamadas
    
    def getcantidadminutos(self):
        return self.__cantidadminutos
    
    def __str__(self):
        return super().__str__() + (f"Tipo de Llamadas {self.__tipodellamadas}, Cantidad de Minutos {self.__cantidadminutos}, Precio Final {self.calcularprecio()}")
    
    def obtenermodificador(self):
        if self.__tipodellamadas == "Internacional":
            return 0.2
        elif self.__tipodellamadas =="Locales":
            return -0.075
        else:
            return 0
            
            