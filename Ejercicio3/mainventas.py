from Gestorventas import *
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
    ventas=GestordeVentas()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            ventas.datos()
        elif opcion==2:
            try:
                sucursal=int(input("Ingrese una sucursal, recuerde que es del 1 al 5"))
                if sucursal > 5 or sucursal < 1:
                    raise ValueError("Ingrese un valor de sucursal correcto del 1 al 5")
                ventas.totalfacturacion(sucursal)
            except ValueError as e:
                print(f"ERROR: {e}")
        elif opcion==3:
            diax=input("Ingrese un dia de la semana\n").lower()
            ventas.sucursalmasacumulo(diax)
        elif opcion==4:
            ventas.menosfacturacion()
        elif opcion==5:
            ventas.total()
        opcion=menu()