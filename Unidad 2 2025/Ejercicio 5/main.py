from manejadorbeneficiario import ManejadorBeneficiarios
from manjeadorbecas import ManejadorBecas

def main():
    opcion=None
    try:
        opcion=int(input("""        Menu de Opciones
                        1) Cargar los datos de las Carreras desde el archivo Carreras.csv.
                        
                        2)Cargar los datos de las Facultades desde del archivo Facultades.csv.
                        
                        3)Leer por teclado un tipo de Beca, e informar los beneficiarios de dicha beca y el
importe total que debe disponer la Secretaría para el pago de dicha Beca.
                        
                        4)Leer por teclado un dni, informar si el beneficiario tiene más de una beca,
mostrando nombre y apellido.
                        
                        5)Listar los beneficiarios, ordenados de mayor a menor por Facultad.
                        
                        6)Listar nombre, apellido y promedio de los estudiantes, que poseyendo un
promedio mayor que 8, no poseen beca de ayuda económica.
                        
                        7)Mostrar Todo
                        
                        8)Ordenar
                        
                        0) Salir
                        
                        
                
                        """))
    except ValueError:
        pass
    return opcion

if __name__=="__main__":
    gestorbeneficiario=ManejadorBeneficiarios()
    gestorbecas=ManejadorBecas()
    opcion=main()
    while opcion!=0:
        if opcion==1:
            gestorbeneficiario.cargarcsv()
        elif opcion==2:
            gestorbecas.cargarcsv()
        elif opcion==3:
            becax=input("Ingrese el tipo de beca: ")
            gestorbeneficiario.buscarbeneficiario(gestorbecas, becax)
        elif opcion==4:
            dni=int(input("Ingrese el DNI del beneficiario: "))
            gestorbeneficiario.buscarbeneficiariopordni(dni)
        elif opcion==5:
            gestorbeneficiario.promedio()
        elif opcion==7:
            print("----Becas-----\n")
            gestorbecas.mostrarBecas()
            print("\n----Beneficiarios-----\n")
            gestorbeneficiario.mostrarBeneficiarios()
        elif opcion==8:
            gestorbeneficiario.ordenar()
        else:
            print('Opcion incorrecta')
        opcion=main()
    print('Fin del programa')
    
