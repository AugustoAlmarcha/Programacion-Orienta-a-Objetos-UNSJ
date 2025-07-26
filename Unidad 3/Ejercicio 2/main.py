from clasegestormaterial import ClaseGestorMaterial
from clasegestorladrillo import GestorLadrillos
def main():
    op = None
    try:
        op = int(input("""        Menu de opciones
                        1) Para un identificador de ladrillo ingresado por teclado: Detallar costo y
característica del material solicitado
                        2) Mostrar para cada ladrillo el costo total de fabricación del pedido.
                        3) Para cada uno de los ladrillos fabricados mostrar el detalle asociado con el
siguiente formato:
N° identificador Material Costo asociado
xxxxxxxxx xxxxxxxx xxxxxxxxxxxxx
xxxxxxxxx xxxxxxxx xxxxxxxxxxxxx
xxxxxxxxx xxxxxxxx xxxxxxxxxxxxx
cubierta del edificio.
                        4) Mostrar Todo
                        0) Salir"""))
    except ValueError:
        pass
    return op

if __name__=="__main__":
    gestorladrillos = GestorLadrillos()
    gestormaterial = ClaseGestorMaterial()
    gestormaterial.cargarcsv()
    gestorladrillos.cargarcsv(gestormaterial)
    opcion = main()
    while opcion != 0:
        if opcion == 1:
            idladrillo = int(input("Ingrese el ID del ladrillo: "))
            gestorladrillos.costomaterial(idladrillo)
        elif opcion == 2:
            gestorladrillos.mostrarcostototal()
        elif opcion == 3:
            gestorladrillos.mostrarmaterialesdelladrillo()
        elif opcion == 4:
            gestormaterial.mostrarmaterial()
            gestorladrillos.mostrarladrillos()
        else:
            print("Opción inválida")
        opcion = main()
    print("Fin del programa")