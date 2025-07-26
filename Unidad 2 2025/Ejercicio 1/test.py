from ejercicio import *
def testx():
    Tarjetax = TarjetaSube(int(input("Ingrese el saldo inicial: ")), int(input("Ingrese el numero de tarjeta: ")))
    tarjeta2 = TarjetaSube(input("Ingrese el saldo inicial: "), int(input("Ingrese el numero de tarjeta: ")))
    tarjeta3 = TarjetaSube(input("Ingrese el saldo inicial: "), int(input("Ingrese el numero de tarjeta: ")))
    
    Tarjetax.cargar_saldo(float(input("Ingrese el importe a cargar: ")))
    Tarjetax.pagar_pasaje(int(input("Ingrese el importe del pasaje: ")))
    Tarjetax.consultar_saldo()