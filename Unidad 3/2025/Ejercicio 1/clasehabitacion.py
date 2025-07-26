class Habitacion:
    __numero:int
    __piso:int
    __tipodehabitacion:str
    __precio:float
    __disponible:bool
    
    def __init__(self, numero: int, piso: int, tipodehabitacion: str, precio: float, disponible: bool = True):
        self.__numero = numero
        self.__piso = piso
        self.__tipodehabitacion = tipodehabitacion
        self.__precio = precio
        self.__disponible = disponible
    
    def getNumero(self):
        return self.__numero
    
    def getPiso(self):
        return self.__piso
    
    def getTipoDeHabitacion(self):
        return self.__tipodehabitacion
    
    def getPrecio(self):
        return self.__precio
    
    def getDisponible(self):
        return self.__disponible
    
    def setDisponible(self, disponible: bool):
        self.__disponible = disponible
    
    def __str__(self):
        return f"\nNumero: {self.__numero}, Piso: {self.__piso}, Tipo: {self.__tipodehabitacion}, Precio: {self.__precio}, Disponible: {self.__disponible}"
