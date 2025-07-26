class MaterialRefractario:
    __material:int
    __caracteristicas:str
    __cantidadutilizada:float
    __costoadicional:float
    
    def __init__(self, material, caracteristicas, cantidadutilizada, costoadicional):
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cantidadutilizada = cantidadutilizada
        self.__costoadicional = costoadicional
    
    def getMaterial(self):
        return self.__material
    
    def getCaracteristicas(self):
        return self.__caracteristicas
    
    def getCantidadUtilizada(self):
        return self.__cantidadutilizada
    
    def getCostoAdicional(self):
        return self.__costoadicional
    
    def __str__(self):
        return f"Material: {self.__material}, Caracteristicas: {self.__caracteristicas}, Cantidad Utilizada: {self.__cantidadutilizada}, Costo Adicional: {self.__costoadicional}"
    
    