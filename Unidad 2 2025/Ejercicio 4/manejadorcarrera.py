from clasecarrera import Carrera
import numpy as np
import csv

class ManejadorCarrera:
    __arreglocarrera:np.ndarray
    __cantidad:int
    __dimension:int
    __incremento:int
    
    def __init__(self):
        self.__cantidad=0
        self.__dimension=10
        self.__incremento=5
        self.__arreglocarrera=np.zeros(self.__dimension,dtype=Carrera)
        
    def agregarcarrera(self,carrera):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglocarrera.resize(self.__dimension)
        self.__arreglocarrera[self.__cantidad]=carrera
        self.__cantidad+=1
        
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 4\Carreras.csv")
            reader=csv.reader(archivo,delimiter=";")
            next(reader)
            for fila in reader:
                self.agregarcarrera(Carrera(int(fila[0]),fila[1].lower(),fila[3],fila[2],fila[4],int(fila[5])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
    
    def mostrarcarreras(self):
        for i in range(self.__cantidad):
            print(self.__arreglocarrera[i])
            
    def quefacultad(self,facultad):
        band=False
        i=0
        nombre=input("Ingrese el nombre de la carrera que busca").lower()
        while band is False and i < self.__cantidad:
            if nombre == self.__arreglocarrera[i].getnombre():
                nombrefacultad=facultad.buscarfacultad(self.__arreglocarrera[i].getcodigofacultad())
                band=True
            i+=1
        if band is False or nombrefacultad is None:
            print("No se encontro la carrera buscada")
        else:
            print(f"La carrera ingresada se encuentra en la facultad cuyo nombre es {nombrefacultad}")
            
    def ordenar(self):
        self.__arreglocarrera[:self.__cantidad] = sorted(self.__arreglocarrera[:self.__cantidad])
    
    def cantidadcarrerasx(self, facultades):
        i = 0
        band = False
        while i < self.__cantidad:
            cod_facultad = self.__arreglocarrera[i].getcodigofacultad()
            facultadcompleta = facultades.contarfacultad(cod_facultad)
            if facultadcompleta is not None:
                ya_mostrada = False
                j = 0
                while j < i and not ya_mostrada:
                    if self.__arreglocarrera[j].getcodigofacultad() == cod_facultad:
                        ya_mostrada = True
                    j += 1
                if not ya_mostrada:
                    cont = 0
                    k = 0
                    while k < len(self.__arreglocarrera):
                        if self.__arreglocarrera[k].getcodigofacultad() == cod_facultad:
                            cont += 1
                        k += 1
                    print(f"La cantidad de carreras que tiene la {facultadcompleta.getnombre()} es de {cont}")
                    band = True
            i += 1
            
    def mostrarcarrerasespecifico(self,facultad):
        i=0  
        print(f"En la universidad {facultad.getnombre()}")
        while i<self.__cantidad:
            if facultad.getcodigofacultad() == self.__arreglocarrera[i].getcodigofacultad():
                print(f"Se cursa la carrera de {self.__arreglocarrera[i].getnombre()} cuya duracion es {self.__arreglocarrera[i].getduracion()}")
            i+=1
        
                    


    
            
                
                
                
                
            
                
        

# if __name__=="__main__":
#     carrerax=ManejadorCarrera()
#     carrerax.cargarcsv()
#     carrerax.mostrarcarreras()
            
    