from cajadeahorro import *
class Test():
    @staticmethod
    def ejecutartest():
        Caja1=CajadeAhorro(input("Ingrese el numero de cuenta"), input("Ingrese su cuil"),input("Ingrese su Apellido"), input("Ingrese su nombre"), float(input("Ingrese su saldo actual")))
        Caja2=CajadeAhorro(input("Ingrese el numero de cuenta"), input("Ingrese su cuil"),input("Ingrese su Apellido"), input("Ingrese su nombre"), float(input("Ingrese su saldo actual")))
        Caja3=CajadeAhorro(input("Ingrese el numero de cuenta"), input("Ingrese su cuil"),input("Ingrese su Apellido"), input("Ingrese su nombre"), float(input("Ingrese su saldo actual")))
        
        Caja1.mostrarDatos()
        Caja2.mostrarDatos()
        Caja3.mostrarDatos()
        
        Caja1.extraer(int(input("Ingrese el monto a extraer")))
        Caja1.depositar(int(input("Ingrese el monto que desea depositar")))
        Caja1.mostrarDatos()