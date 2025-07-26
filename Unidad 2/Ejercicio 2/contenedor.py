from cajadeahorro import *
class Contenedor:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
    
    def crearcuenta(self):
        cantidad=int(input("Ingrese cuantas cuentas quiere crear\n"))
        i=0
        while i < cantidad: 
            Cajax=CajadeAhorro(i+1, input("Ingrese su cuil"),input("Ingrese su Apellido"), input("Ingrese su nombre"), float(input("Ingrese su saldo actual")))
            self.__lista.append(Cajax)
            i+=1
    
    def mostrarlista(self):
        for item in self.__lista:
            print (f"{item}")
    
    def buscarcuenta(self,cuil):
        i=0
        band=False
        while i < len(self.__lista) and band is False:
            if cuil == self.__lista[i].getcuil():
                band=True
                print("Cuenta encontrada")
            else:
                i+=1
        if band is False:
            return -1
        else:
            return i
    
    def mostrardatos(self, i):
        self.__lista[i].mostrarDatos()
                
        
            
            
if __name__=="__main__":
    contenedor = Contenedor()
    contenedor.crearcuenta()
    contenedor.mostrarlista()
    cuil=input("Ingrese cuil de la cuenta que busca\n")
    i=contenedor.buscarcuenta(cuil)
    if i == -1:
        print("No se encontró la cuenta con ese CUIL.")
    else:
        contenedor.mostrardatos(i)
