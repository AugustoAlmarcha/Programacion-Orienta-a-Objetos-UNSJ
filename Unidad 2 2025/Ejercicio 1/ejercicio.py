class TarjetaSube:
    __saldo:float
    __numerotarjeta:int
    
    def __init__(self, saldo:float, numerotarjeta:int):
        self.__saldo = saldo
        self.__numerotarjeta = numerotarjeta
    
    def getSaldo(self):
        return self.__saldo
    
    def getNumeroTarjeta(self):
        return self.__numerotarjeta
    
    def __str__(self):
        return f"Tarjeta Sube {self.__numerotarjeta} con saldo {self.__saldo}"
    
    def cargar_saldo(self,importe:float):
        self.__saldo += importe
    
    def pagar_pasaje(self, importe:int):
        if self.__saldo >= importe:
            self.__saldo -= importe
            print(f"Pasaje pagado. Saldo restante: {self.__saldo}")
        else:
            print("Saldo insuficiente para pagar el pasaje.")
    
    def consultar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")
            
    