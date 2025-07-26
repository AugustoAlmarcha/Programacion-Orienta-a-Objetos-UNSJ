from gestordemotos import *
from gestordepedidos import *

def menu():
    op=None
    try:
        op=int(input("""
                            Menú de Opciones
            [1] Cargar nuevos pedidos, leer los datos por teclado, y asignar a una moto el pedido, al
solicitar la patente de la moto para asignarla, validar que la moto existe.
            [2] Leer por teclado número de patente, identificador de pedido, y tiempo real de entrega,
modificar en el Gestor de Pedidos, el tiempo real de entrega para ese pedido.
            [3] Leer por una patente de una moto, mostrar los datos del conductor y el tiempo promedio
real de entrega de los pedidos que hizo.
            [4] Generar un listado para cada moto, para el pago de comisiones a los conductores de las
motos:
            [5] Mostrar
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    motox=GestorMoto()
    motox.cargarcsv()
    pedidos=Gestorpedidos()
    pedidos.cargar()
    pedidos.ordenar()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            patentex=input("Ingrese la patente del nuevo pedido")
            si = motox.existe(patentex)
            if si:
                identificador = int(input("Ingrese el identificador del pedido"))
                comida=input("Ingrese la comida del pedido")
                tiempoestimado=float(input("Ingrese el tiempo estimado de espera del pedido"))
                precio=float(input("Ingrese el precio"))
                pedidos.agregar(Pedido(patentex,identificador,comida,tiempoestimado,precio))
            else:
                print("La patente ingresada no existe")
        elif opcion==2:
            pedidos.modificar()
        elif opcion==3:
            patentey=input("Ingrese la patente de la moto que busca")
            x=motox.mostrardatos(patentey)
            if not x:
                print("No se encontro moto registrada con esa patente")
            else:
                pedidos.tiempopromedio(patentey)   
        elif opcion==4:
            pedidos.listado(motox)
        elif opcion==5:
            print("---Motos---")
            motox.mostrar()
            print("---Pedidos---")
            pedidos.mostrar()
        elif opcion==6:
            pedidos.lista(motox)
        opcion=menu()