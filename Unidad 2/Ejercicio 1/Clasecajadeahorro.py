class Cajadeahorro:
    __numero:str
    __cuil:str
    __apellido:str
    __nombre:str
    __saldo:int
    
    def __init__(self, numero,cuil,apellido,nombre,saldo):
        self.__numero=numero
        self.__cuil= cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__saldo= saldo
    
    def __str__(self):
        return f"Apellido: {self.__apellido}\nNombre: {self.__nombre}\nCUIL: {self.__cuil}, Número de Cajero: {self.__numero}\nSaldo: {self.__saldo}"
    
    def getnumero(self):
        return self.__numero
    
    def extraer(self,extraccion):
        if extraccion < self.__saldo:
            self.__saldo -= extraccion
            return f"Se ha extraido ${extraccion} de la cuenta del Cajero {self.__numero}"
        else:
            return f"No hay saldo suficiente para extraer ${extraccion} de la cuenta del Cajero {self.__numero}"
        
    def depositar(self,importe):
        if importe > 0:
            self.__saldo += importe
            return f"Se ha depositado ${importe} en la cuenta del Cajero {self.__numero}"
        else:
            return f"No se puede depositar ${importe} en la cuenta del Cajero {self.__numero}"