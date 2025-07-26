from claseplanes import Planes

class Television(Planes):
    __cantidadcanalesnacionales:int
    __cantidadcanalesinternacionales:int
    
    def __init__(self,nombre,duracion,cobertura,precio,nacional,internacional):
        super().__init__(nombre,duracion,cobertura,precio)
        self.__cantidadcanalesnacionales=nacional
        self.__cantidadcanalesinternacionales=internacional
        
    def __str__(self):
        return super().__str__() + (f"Cantidad canales nacionales {self.__cantidadcanalesnacionales}, Cantidad de canales internacionales {self.__cantidadcanalesinternacionales}, Precio Final: {self.calcularprecio()}")
    
    def getnacional(self):
        return self.__cantidadcanalesnacionales
    
    def getinternacional(self):
        return self.__cantidadcanalesinternacionales
    
    def obtenermodificador(self):
        if self.__cantidadcanalesinternacionales > 10:
            return 0.15
        else:
            return 0