import csv
from clasenacimiento import *

class GestorNacimientos:

    __listanacimiento:list
    
    def __init__(self):
        self.__listanacimiento=[]
        
    def agregarNacimiento(self,nacimiento):
        self.__listanacimiento.append(nacimiento)
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio\Nacimientos.csv")
            reader=csv.reader(archivo,delimiter=';')
            for fila in reader:
                self.agregarNacimiento(Nacimiento(fila[0],fila[1],fila[2],fila[3],float(fila[4]),int(fila[5])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encontro")
        except Exception as error:
            print(f"Error en la carga de datos {error}")
            
    def mostrar(self):
        for nacimiento in self.__listanacimiento:
            print(nacimiento)
            
    def mostrarnacimientos(self,dni):
        for nacimiento in self.__listanacimiento:
            if nacimiento.getDni()==dni:
                if nacimiento.getTipoParto()=="N":
                    print("Parto natural")
                else:
                    print("Parto cecarea")
                print(f"{nacimiento.getPeso():.3f}, {nacimiento.getAltura()}")
    
    def partosmultiples(self,mama):
        band=False
        i=0
        while i<len(self.__listanacimiento):
            j=i+1
            while j<len(self.__listanacimiento):
                if self.__listanacimiento[i]==self.__listanacimiento[j]:
                    mama.mostrartodomamas(self.__listanacimiento[i].getDni())
                    band=True
                j+=1
            i+=1
            
# if __name__=="__main__":
#     gestor=GestorNacimientos()
#     gestor.cargarcsv()
#     gestor.mostrar()
        
        