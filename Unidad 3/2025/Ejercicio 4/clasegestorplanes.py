from claseplanes import Planes
from clasetelefonia import Telefonia
from clasetelevision import Television
import csv

class GestorPlanes:
    __listaplanes:list
    
    def __init__(self):
        self.__listaplanes = []
        
    def agregar(self,plan):
        self.__listaplanes.append(plan)
        
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 3\2025\Ejercicio 4\planes.csv")
            
            reader = csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                if fila[0] == "M":
                    self.agregar(Telefonia(fila[1], int(fila[2]), fila[3], float(fila[4]),fila[5], int(fila[6])))
                elif fila[0] == "T":
                    self.agregar(Television(fila[1], int(fila[2]), fila[3], float(fila[4]),int(fila[5]), int(fila[6])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as e:
            print("Error: ", str(e))
    
    def mostrar(self):
        for plan in self.__listaplanes:
            if isinstance(plan,Telefonia):
                print(f"Telefonia:\n {plan}")
            elif isinstance(plan,Television):
                print(f"Television:\n {plan}")
                
    def mostratipo(self,posicion):
        try:
            if isinstance(self.__listaplanes[posicion],Telefonia):
                print(f"En la posicion {posicion} se encuentra un plan de Telefonia")
            elif isinstance(self.__listaplanes[posicion], Television):
                print(f"En la posicion {posicion} se encuentra un plan de Television")
        except IndexError:
            print("La posicion ingresada no existe")
    
    def contarplanes(self,cobertura):
        i=0
        band=False
        contador=0
        while i<len(self.__listaplanes):
            if self.__listaplanes[i].getcobertura().lower() == cobertura:
                band=True
                contador+=1
            i+=1
        if band is True:
            print(f"La cantidad de planes con cobertura {cobertura} es de {contador}")
        else:
            raise ValueError("No hay planes con la cobertura ingresada")
    
    def mostrarcompania(self,cantidad):
        i=0
        band=False
        while i<len(self.__listaplanes):
            if isinstance(self.__listaplanes[i],Television) and self.__listaplanes[i].getinternacional() >= cantidad:
                print(f"La compañia {self.__listaplanes[i].getnombre()} ofrece {self.__listaplanes[i].getinternacional()} canales internacionales")
                band=True
            i+=1
        if band is False:
            print("No hay planes con esa cantidad de canales internacionales")
    
    def mostrar4(self):
        for plan in self.__listaplanes:
            plan.mostrarresumen()
                
                
    
# if __name__=="__main__":
#     gestor = GestorPlanes()
#     gestor.cargarcsv()
#     gestor.mostrar()