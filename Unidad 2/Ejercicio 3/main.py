from clasegestorventas import *

def menu():
    op=None
    try:
        op=int(input("""
                            Menú de Opciones
            [1] Ingresar datos de la venta.
            [2] Ingrese sucursal y se le dira el total de la facturacion para esa sucursal 
            [3] Ingrese un dia de la semana y se le dira que sucursal facturo mas ese dia
            [4] Calcular la sucursal con menos facturación durante toda la semana.
            [5] Calcular el total facturado por todas las sucursales durante toda la semana.
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    ventas=GestorVentas()
    opcion=menu()
    ventas.mostrararreglo()
    while opcion!=0:
        if opcion==1:
            ventas.agregarventa()
        elif opcion==2:
            ventas.totalsucursal()
        elif opcion==3:
            ventas.totaldia()
        elif opcion==4:
            ventas.menosfacturacion()
        elif opcion==5:
            ventas.total()
        elif opcion==6:
            ventas.mostrararreglo()
        opcion=menu()