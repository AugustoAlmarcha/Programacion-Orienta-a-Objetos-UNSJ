from gestorrutas import *
from gestorvehiculos import *

def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Agregar nuevos vehículos a la instancia de la clase de control definida antes.
En el caso de agregar un Camión, deberán seleccionarse las Rutas que recorre
desde el objeto control de Rutas, marcando como asignadas las rutas del
controlador de rutas, pues una Ruta no puede ser recorrida por más de un
Camión.
Para buscar una ruta, debe ingresar el código de ruta, buscarla en el
controlador de Rutas, si no existe al Ruta, lanzar una excepción (IndexError),
en caso de que exista y no esté asignada a un Camión, asignarla, y modificar el
estado del atributo rutaAsignada, y en el caso de que exista la Ruta, pero esté
asignada a un Camión, lanzar otra excepción (IOError).
                        2) Leer por teclado una matrícula de un vehículo, buscarlo en el controlador de
Vehículos, mostrar toda su información, incluidas las rutas asociadas. Si no se
encuentra, lanzar una excepción (Exception).
                        3) Indicar para cada vehículo la matricula, modelo y el costo total de alquiler del
vehículo.
                        4) Controlar las excepciones.
                        5)Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestorvehiculos = Gestorvehiculos()
    gestorrutas= gestorruta()
    gestorrutas.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            opcionx= input("Que tipo de vehiculo desea agregar (Camion,Automovil)): ").strip().lower()
            if opcionx == "camion" or opcionx == "automovil":
                matricula = input("Ingrese matricula del vehiculo: ").strip()
                modelo = input("Ingrese modelo del vehiculo: ").strip()
                costoporkm= float(input("Ingrese el costo por kilometro"))
                cantidaddediasdealquiler= int(input("Ingrese la cantidad de dias que se alquilara"))
            if opcionx == "camion":
                capacidadmaxima= float(input("Ingrese la capacidad maxima de carga permitida"))
                cantidadrealtransportada=float(input("Ingrese la cantidad real transportada"))
                camion=(Camiones(matricula,modelo,costoporkm,cantidaddediasdealquiler,capacidadmaxima,cantidadrealtransportada))
                codigoruta= int(input("Ingrese el codigo de las rutas que quiere recorrer termine con un 0"))
                while codigoruta != 0:
                    try:
                            gestorrutas.asignarruta(camion,codigoruta)
                    except IndexError:
                        print("La ruta no existe")
                    except IOError:
                        print("La ruta ya esta asignada a un camion")
                    codigoruta= int(input("Ingrese el codigo de las rutas que quiere recorrer termine con un 0"))
                gestorvehiculos.agregarvehiculo(camion)
                print("Camion cargado correctamente")
            elif opcionx == "automovil":
                pasajerosmax= int(input("Ingrese el maximo de pasajeros"))
                cantidadpasajerosreal=int(input("Ingrese la cantidad de pasajeros real"))
                gestorvehiculos.agregarvehiculo(Automovil(matricula,modelo,costoporkm,cantidaddediasdealquiler,pasajerosmax,cantidadpasajerosreal))
            else:
                print("Tipo de vehiculo no reconocido.")
        elif opcion == 2:
            matricula= input("Ingrese matricula del vehiculo: ").strip()
            try:
                gestorvehiculos.buscarvehiculo(matricula)
            except Exception as e:
                print("Error: ", e)
        elif opcion == 3:
            try:
                gestorvehiculos.indicar()
            except Exception as e:
                print("Error: ", e)
        elif opcion == 4:
            pass
        elif opcion == 5:
            gestorrutas.mostrar()
            gestorvehiculos.mostrarvehiculos()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")