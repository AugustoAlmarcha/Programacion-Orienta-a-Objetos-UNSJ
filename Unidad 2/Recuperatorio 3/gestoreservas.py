import csv
from clasereserva import *

class GestorReservas:
    __listareserva:list
    
    def __init__(self):
        self.__listareserva = []
        
    def agregarReserva(self, reserva:Reserva):
        self.__listareserva.append(reserva)
        
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio 3\Reservas.csv")
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                self.agregarReserva(Reserva(int(fila[0]), fila[1], int(fila[2]), fila[3], int(fila[4]), int(fila[5]), int(fila[6])))
            archivo.close()
        except Exception as e:
            print(f'Error al cargar el archivo: {e}')
        except FileNotFoundError:
            print('No se encontro el archivo')
            
    def mostrar(self):
        for reserva in self.__listareserva:
            print(reserva)
    
    def estareservada(self, numerocabaña):
        i=0
        band=False
        while i < len(self.__listareserva) and band is False:
            if self.__listareserva[i].getCabañaAsignada() == numerocabaña:
                band=True
            i+=1
        return band
    
    def reservas(self, cabana):
        i=0
        band=False
        importetotal=0
        importediario=0
        fecha=input('Ingrese la fecha con el siguiente formato dd/m/años:  ')
        while i < len(self.__listareserva):
            if self.__listareserva[i].getFecha() == fecha:
                importediario= cabana.ImportePorDia(self.__listareserva[i].getCabañaAsignada())
                if importediario is not None:
                    print("Numero de Cabaña|Importe Diario|Cantidad de Dias|Importe de la Seña|Importe a Cobrar")
                    print("       ",self.__listareserva[i].getCabañaAsignada() , "      |     " , importediario , " |      " , self.__listareserva[i].getCantidadDias() , "       |     " , self.__listareserva[i].getImporteDeLaSeña() , "     |    " , (importediario * self.__listareserva[i].getCantidadDias()) - self.__listareserva[i].getImporteDeLaSeña())
                    band=True
            i+=1
        if band is False:
            print('No hay reservas para la fecha ingresada')
            
            
    
            
# if __name__=="__main__":
#     gestor=GestorReservas()
#     gestor.cargarcsv()
#     gestor.mostrar()