class CajadeAhorro:
    __nrocuenta:str
    __cuil:str
    __apellido:str
    __nombre:str
    __saldo:float
    
    def __init__(self,numero,cuil,apellido,nombre,saldo):
        self.__nrocuenta=numero
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__saldo=saldo
        
    def mostrarDatos(self):
        print(f"Numero de cuenta: {self.__nrocuenta}, Cuil: {self.__cuil}, Apellido y Nombre: {self.__apellido}, {self.__nombre}, Saldo: {self.__saldo}")
    
    def extraer(self,importe):
        if self.__saldo < importe:
            print(f"No se puede hacer la extraccion le quedaria un saldo de {self.__saldo-importe}")   
        else:
            print("Extraccion realizada con exito")
            self.__saldo-=importe
            print(f"Su saldo actual es de {self.__saldo}")     
    
    def depositar(self,deposito):
        if deposito > 0:
            self.__saldo += deposito
            print(f"Su nuevo saldo es de {self.__saldo}")
        else:
            print("Su deposito es menor a 0, ingrese bien los digitos a ingresar")
    
    