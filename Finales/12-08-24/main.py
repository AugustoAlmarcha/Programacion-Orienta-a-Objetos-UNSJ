from Clasepacientes import Paciente
from claselistapacientes import *

def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) a. Insertar objetos al final de la colección. El estado de los objetos
proviene de un archivo, separado por comas denominado:
“pacientes.csv”. El primer caracter de cada fila del archivo, indica el tipo
de objeto que representa, “P”-Paciente, “O”-Paciente con Obra Social y
“H”-Paciente Hospitalizado.
                        2) Indicar la cantidad de pacientes hospitalizados, cuyo diagnóstico es
neumonía; y la cantidad de pacientes ambulatorios que posee la clínica.
                        3) Mostrar el importe cobrado por la clínica, a todos los pacientes.
                        4) En el programa principal o en el menú, leer por teclado un valor entero,
que representa una posición de la lista, e indicar qué tipo de paciente se
encuentra en esa posición. El método definido en la clase colección,,
debe lanzar la excepción IndexError, en el caso de que la posición esté
fuera de rango.. El programa principal o el menú, quien haya invocado
el método de la colección, debe capturar la excepción y mostrar un
mensaje de error “Índice fuera de rango”.
                        5)En el programa principal o en el menú, leer por teclado un nuevo valor
de consulta, cambiarlo para todos los objetos de la lista.
                        6)Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    lista = ListaPacientes()
    lista.cargarcsv()
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            opcionx= input("Que tipo de paciente desea agregar? (Ambulatorio/Hospitalizado): ").strip().lower()
            if opcionx == "ambulatorio" or opcionx == "hospitalizado":
                nombre = input("Ingrese el nombre del paciente")
                apellido= input("Ingrese el apellido del paciente")
                email = input("Ingrese el email del paciente")
                telefono = input("Ingrese el telefono del paciente")
                if opcionx == "ambulatorio":
                    historial= input("Ingrese el historial medico")
                    alergia= input("Ingrese la alergia del paciente")
                    obrasocial= input("Ingrese la obra social del paciente")
                    lista.agregaralfinal(PacienteAmbulatorio(nombre,apellido,email,telefono,historial,alergia,obrasocial))
                elif opcionx == "hospitalizado":
                    numerohabitacion= int(input("Ingrese el numero de habitacion"))
                    fechaingreso = input("Ingrese la fecha de ingreso")
                    diagnostico = input("Ingrese el diagnostico del paciente")
                    cantidaddiasinternacion= int(input("Ingrese la cantidad de dias de internacion"))
                    importedescartables= float(input("Ingrese el importe en descartables"))
                    lista.agregaralfinal(PacientesHospitalizados(nombre,apellido,email,telefono, numerohabitacion, fechaingreso,diagnostico,cantidaddiasinternacion,importedescartables))
            else:
                print("Tipo de paciente no reconocido.")
        elif opcion == 2:
            lista.cantidad()
        elif opcion == 3:
            lista.mostrartodoslosimportes()
        elif opcion == 4:
            try:
                posicion = int(input("Ingrese la posicion del paciente: "))
                lista.clienteenposicion(posicion)
            except IndexError:
                print("Índice fuera de rango")  
        elif opcion==5:
            nuevovalor= float(input("Ingrese un nuevo valor de consulta"))
            Paciente.valorconsulta = nuevovalor
        elif opcion == 6:
            lista.mostrar()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")