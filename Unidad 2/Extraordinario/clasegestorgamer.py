import csv


from clasegamer import *


class GestorGamer:
    __lista:list
    
    def __init__(self):
        self.__lista = []
        
    def agregarGamer(self,gamer:Gamer):
        self.__lista.append(gamer)
        
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\Extraordinario\gammers.csv")
            reader=csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarGamer(Gamer(int(fila[0]),int(fila[1]),fila[2],fila[3],fila[4],fila[5],int(fila[6]),int(fila[7])))
            archivo.close()
        except Exception as e:
            print(f'Error al cargar el archivo: {e}')
        except FileNotFoundError:
            print('No se encontro el archivo')
            
    def mostrar(self):
        for i in self.__lista:
            print(i)
    
    def BuscarGamer(self,dni):
        i=0
        while i<len(self.__lista):
            if self.__lista[i].getDni()==dni:
                return self.__lista[i]
            i+=1
        return None
    
    def BuscarGamerporId(self,id):
        i=0
        while i<len(self.__lista):
            if id == self.__lista[i].getIdJugador():
                return self.__lista[i]
            i+=1
        return None
            
# if __name__=="__main__":
#     gestor=GestorGamer()
#     gestor.cargarcsv()
#     gestor.mostrar()