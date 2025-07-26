import csv
from clasevisualizacion import *

class GestorVisualizaciones:
    __listavisualizacion:list
    
    def __init__(self):
        self.__listavisualizacion=[]
        
    def agregarVisualizacion(self,visualizacion:Visualizacion):
        self.__listavisualizacion.append(visualizacion)
        
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Recuperatorio 2\Visualizaciones.csv")
            reader=csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregarVisualizacion(Visualizacion(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4])))
            archivo.close()
        except FileNotFoundError:
            print("No se pudo abrir el archivo")
        except Exception as e:
            print(e)
    
    def mostrar(self):
        for visualizacion in self.__listavisualizacion:
            print(visualizacion)
            
    def cantidadtotalminutos(self,miembros):
        i=0
        total=0
        band=False
        correo=input("Ingrese el correo del miembro que busca")
        while i<len(self.__listavisualizacion):
            id=miembros.buscarmiembro(correo)
            if id is not None:
                if id == self.__listavisualizacion[i].getIDMiembro():
                    total+=self.__listavisualizacion[i].getMinutos()
                    band=True
                i+=1
            else:
                print("No se encontro usuario con ese correo")
                break
        if band==True:
            print(f"El total de minutos que vio {correo} es {total}")
            
    def visualizacionsimultanea(self,miembro):
        i=0
        band=False
        while i<len(self.__listavisualizacion):
            j=i+1
            while j<len(self.__listavisualizacion):
                if self.__listavisualizacion[i]==self.__listavisualizacion[j]:
                    band=True
                    miembrox=miembro.buscarporid(self.__listavisualizacion[i].getIDMiembro())
                    if miembro is not None:
                        print(f"{miembrox.getNya()},{miembrox.getCorreo()} tiene visualizaciones simultaneas")
                    else:
                        print("No se encontro miembro con ese id")
                j+=1
            i+=1
        if band==False:
            print("No se encontraron visualizaciones simultaneas")
    
            
            
            
                
                

                
                
            
            
            
    
# if __name__ == '__main__':
#     gv=GestorVisualizaciones()
#     gv.cargarcsv()
#     gv.mostrar()
    
    