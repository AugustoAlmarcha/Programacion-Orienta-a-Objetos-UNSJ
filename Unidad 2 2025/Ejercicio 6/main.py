from clasemanejadoratenciones import *
from clasemanejadorpacientes import *
def main():
    opcion = None
    try: 
        opcion = int(input("""        Menu de Opciones
                        1) Leer por teclado una fecha, e informar las atenciones realizadas en dicha fecha y el 
importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha. 
                        
                        2) Leer por teclado un dni, e informar Nombre y apellido, y cantidad de atenciones 
que tuvo. 
                        
                        3) Listar nombre, apellido de los pacientes que no tuvieron ninguna atención
                        
                        4) Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad.
                        
                        5) Mostrar Todo
                        
                        0) Salir
                        
                        """))
    except ValueError:
        pass
    return opcion

if __name__ == "__main__":
    manejadorPacientes = ManejadorPacientes()
    manejadorAtenciones = ManejadorAtenciones()
    manejadorPacientes.cargarcsv()
    manejadorAtenciones.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            fecha = input("Ingrese la fecha (dd/mm/yyyy): ")
            manejadorAtenciones.atencionesPorFecha(fecha, manejadorPacientes)
        elif opcion == 2:
            dni = int(input("Ingrese el DNI del paciente: "))
            manejadorAtenciones.cantidadatenciones(dni, manejadorPacientes)
        elif opcion == 3:
            manejadorPacientes.pacientesSinAtencion(manejadorAtenciones)
        elif opcion == 4:
            manejadorPacientes.ordenarPacientes()
        elif opcion == 5:
            print("----Pacientes-----\n")
            manejadorPacientes.mostrarPacientes()
            print("\n----Atenciones-----\n")
            manejadorAtenciones.mostrarAtenciones()
        else:
            print("Opción no válida.")
        opcion = main()