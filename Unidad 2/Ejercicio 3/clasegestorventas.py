import numpy as np

class GestorVentas:
    __arreglo:np.ndarray
    
    def __init__(self):
        self.__arreglo = np.zeros([5,7],dtype=float)
        
    def agregarventa(self):
        dia=int(input("Ingrese el dia de la venta:")) - 1
        numerosucursal= int(input("Ingrese el numero de la sucursal")) - 1 
        importe= float(input("Ingrese el importe de la factura"))
        
        self.__arreglo[numerosucursal,dia]+=importe
    
    def mostrararreglo(self):
        for item in self.__arreglo:
            print(item)
            
    def totalsucursal(self):
        sucursal=int(input("Ingrese el numero de la sucursal")) - 1
        total=0
        for i in range(7):
            total+=self.__arreglo[sucursal,i]
        print(f"El total recaudado por la sucursal {sucursal+1} es: {total}")
        
    def totaldia(self):
        dia=int(input("Ingrese el dia de la semana"))-1
        max=0
        for i in range(5):
            if max < self.__arreglo[i,dia]:
                max = self.__arreglo[i,dia]
                aux=i+1
        print(f"La sucursal que mas facturo el dia {dia+1} es la {aux} con un total de {max}")
        
    def menosfacturacion(self):
        min=999999
        calculo=0
        for i in range(5):
            for j in range(7):
                calculo += self.__arreglo[i][j]
            if min > calculo:
                min=calculo
                aux=str(i+1)
            elif min == calculo:
                aux+= f"; {i+1}"
            print(f"La sucursal {i+1} recaudo {calculo} pesos en la semana")    
            calculo=0
        print(f"La sucursal que menos recaudo fue la sucursal {aux} recaudando {min} pesos en la semana")
        
    
    def total(self):
        total = self.__arreglo.sum()
        print(f"El total de la facturación en todas las sucursales y días es: {total:.2f}")

        

        
    
    

        
        