from clasepublicaciones import Publicaciones

class CD(Publicaciones):
    __tiemporeproduccionminutos:int
    __nombrenarrador:str
    
    def __init__(self, titulo, categoria, precio, tiemporeproduccionminutos, nombrenarrador):
        super().__init__(titulo, categoria, precio)
        self.__tiemporeproduccionminutos = tiemporeproduccionminutos
        self.__nombrenarrador = nombrenarrador

    def getTiempoProduccion(self):
        return self.__tiemporeproduccionminutos

    def getNombreNarrador(self):
        return self.__nombrenarrador

    def __str__(self):
        return super().__str__() + f", Tiempo de Produccion: {self.__tiemporeproduccionminutos} minutos, Narrador: {self.__nombrenarrador}, Precio Final: {self.calcularPrecio()}"
    
    def calcularPrecio(self):
        return self.getPrecio() + (self.getPrecio() * 0.1)
    