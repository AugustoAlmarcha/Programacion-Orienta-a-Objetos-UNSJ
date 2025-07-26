from clasegestorconexiones import *
from clasegestorgamer import *

def main():
    opcion=None
    try:
        opcion=int(input("""        Menu de Opciones
                        1) En el programa principal, leer por teclado el DNI de un Gammer, 
                        si no existe emitir un mensaje que advierta de tal situación, 
                        si existe, mostrar un listado de las conexiones, con el siguiente formato.
                        
                        2)En el programa principal, leer por teclado el nombre de un juego, si no existe, mostrar un mensaje que advierta de tal situación, 
                        si existe, mostrar: dirección IP de conexión, nombre y apellido, alias, tipo de plan de los usuarios que han jugado dicho juego.
                        
                        3)La empresa, quiere advertir a los gammer’s que utilizan el servicio Basico que no 
                        pueden conectarse simultáneamente a los juegos en más de una dirección IP, en la misma fecha y hora de inicio. 
                        Para ello le solicita a usted que emita un listado de jugadores con servicio Basico, que se conectan en IP’s distintas, simultáneamente.
                        
                        4)Mostrar
                        
                        0) Salir
                        
                        
                
                        """))
    except ValueError:
        pass
    return opcion

if __name__=="__main__":
    gestorconexiones=Gestorconexiones()
    gestorgamer=GestorGamer()
    gestorconexiones.cargarcsv()
    gestorgamer.cargarcsv()
    opcion=main()
    while opcion!=0:
        if opcion==1:
            dni=int(input('Ingrese DNI del gamer que busca: '))
            gestorconexiones.mostrarConexiones(dni,gestorgamer)
        elif opcion==2:
            nombrejuego= input("Ingrese el Nombre de un Juego")
            gestorconexiones.BuscarJuego(nombrejuego,gestorgamer)
        elif opcion==3:
            gestorconexiones.Listadomismo(gestorgamer)
        elif opcion==4:
            print("Conexiones")
            gestorconexiones.mostrar()
            print("Gamers")
            gestorgamer.mostrar()
        elif opcion==5:
            gestorconexiones.ordenar()
        else:
            print('Opcion incorrecta')
        opcion=main()
    print('Fin del programa')