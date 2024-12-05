import numpy as np
class GestordeVentas:
    __arreglo: np.ndarray
    
    def __init__(self):
        self.__arreglo = np.zeros([5,7], dtype=float)
        
    def datos(self):
        dias = {
            "lunes": 1,
            "martes": 2,
            "miercoles": 3,
            "jueves": 4,
            "viernes": 5,
            "sabado": 6,
            "domingo": 7
        }
        try:
            diastr=input("Ingrese un el dia de la semana que sea la facturacion").lower()
            dia= dias.get(diastr, None)
            if dia is None:
                raise ValueError("Ingrese correctamente el dia")
            numerosucursal= int(input("Ingrese el numero de la sucursal"))
            if numerosucursal < 1 or numerosucursal > 5:
                raise ValueError("Número de sucursal fuera de rango. Debe estar entre 1 y 5.")
            importe = float(input(f"Ingrese el importe para la factura de la sucursal {numerosucursal} del dia {diastr}"))
            self.__arreglo[numerosucursal-1][dia-1]+=importe
            self.mostrar()
        except ValueError as e:
            print(f"ERROR {e}")
        
    
    def totalfacturacion(self,sucursal):
        acumular=0
        for datox in self.__arreglo[sucursal-1]:
            acumular+=datox
        print(f"La facturacion total de esa semana es de {acumular}")
    
    def sucursalmasacumulo(self,diax):
        dias = {
            "lunes": 1,
            "martes": 2,
            "miercoles": 3,
            "jueves": 4,
            "viernes": 5,
            "sabado": 6,
            "domingo": 7
        }
        try:
            dia= dias.get(diax, None)
            if dia is None:
                raise ValueError("Ingrese correctamente el dia")
            else:
                columna_dia = self.__arreglo[:, dia - 1]
                sucursal_max = np.argmax(columna_dia)
                print(f"La sucursal que más facturó el día {diax} es la sucursal {sucursal_max + 1} con un total de {columna_dia[sucursal_max]:.2f}.")        
        except ValueError as e:
            print(f"ERROR: {e}")
            
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
    
    def mostrar(self):
        print(self.__arreglo)
        
        
        
    
        
        