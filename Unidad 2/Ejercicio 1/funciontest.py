from Clasecajadeahorro import *

def test():
    objeto1= Cajadeahorro(input("Ingrese numero de cuenta"), input("Ingrese cuil"), input("Ingrese Apellido"), input("Ingrese Nombre"),  int(input("Ingrese Saldo")))
    objeto2= Cajadeahorro(input("Ingrese numero de cuenta"), input("Ingrese cuil"), input("Ingrese Apellido"), input("Ingrese Nombre"),   int(input("Ingrese Saldo")))
    objeto3=Cajadeahorro(input("Ingrese numero de cuenta"), input("Ingrese cuil"), input("Ingrese Apellido"), input("Ingrese Nombre"),   int(input("Ingrese Saldo")))
    
    print(objeto1)
    print(objeto2)
    print(objeto3)
    
    numero=input("Ingrese el numero de cuenta que quiere realizar la operacion")
    while True:
        if numero==objeto1.getnumero():
            operacion=input("Ingrese la operacion que desea realizar")
            if operacion=="depositar":
                objeto1.depositar(input("Ingrese la cantidad a depositar"))
                break
            elif operacion=="extraer":
                objeto1.extraer(input("Ingrese la cantidad a extraer"))
                break
            else:
                print("No existe la operacion que desea realizar es depositar o extraer")
                break
        elif numero==objeto2.getnumero():
            operacion=input("Ingrese la operacion que desea realizar")
            if operacion=="depositar":
                objeto2.depositar(int(input("Ingrese la cantidad a depositar")))
                print(objeto2)
                break
            elif operacion=="extraer":
                objeto1.extraer(input("Ingrese la cantidad a extraer"))
                break
            else:
                print("No existe la operacion que desea realizar es depositar o extraer")
                break
        elif numero==objeto3.getnumero():
            operacion=input("Ingrese la operacion que desea realizar")
            if operacion=="depositar":
                objeto1.depositar(input("Ingrese la cantidad a depositar"))
                break
            elif operacion=="extraer":
                objeto1.extraer(input("Ingrese la cantidad a extraer"))
                break
            else:
                print("No existe la operacion que desea realizar es depositar o extraer")
                break
        else:
            print("No existe cuenta con ese numero")
        
        
        
            
            
            