from clasevehiculos import Vehiculo

class Camiones(Vehiculo):
    __capacidadmaximacarga:float
    __cantidadtransportada:float
    __listarutas: list
    
    def __init__(self,matricula,modelo,costo,dias,capacidad,cantidad):
        super().__init__(matricula,modelo,costo,dias)
        self.__capacidadmaximacarga = capacidad
        self.__cantidadtransportada = cantidad
        self.__listarutas = []
        
    def agregarruta(self, ruta):
        self.__listarutas.append(ruta)
        
    def getcapacidad(self):
        return self.__capacidadmaximacarga
    
    def getcantidadtransportada(self):
        return self.__cantidadtransportada
    
    def __str__(self):
        ruta = ", \n".join([str(rutax) for rutax in self.__listarutas]) if self.__listarutas else "No hay rutas"
        return super().__str__() + f"Capacidad maxima de carga: {self.__capacidadmaximacarga}, Cantidad transportada: {self.__cantidadtransportada}, Rutas: {ruta}"
    
    def calculo(self):
        if self.__cantidadtransportada > 4500:
            return self.getCostoXkm() * 0.05
        elif self.__cantidadtransportada <= 4500:
            return self.getCostoXkm() * 0.02
            