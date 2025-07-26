from clasedepartamento import Departamentos
from claseaccidente import *
import csv
class ManejadorDepartamentos:
    __departamentos: list
    
    def __init__(self):
        self.__departamentos = []
    
    def agregar_departamento(self, depa):
        self.__departamentos.append(depa)
    
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Unidad 2\2025\Ejercicio 3\Departamentos.csv")
            reader= csv.reader(archivo,delimiter=';')
            next(reader)
            for fila in reader:
                self.agregar_departamento(Departamentos((int(fila[0])), (fila[1])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo CSV no se encontró.")
        except Exception as e:
            print("Error al leer el archivo CSV:", e)
    
    def mostrardepartamentos(self):
        for departamento in self.__departamentos:
            print(departamento)
            
    def mostraraccidenteespecifico(self,accidentes):
        numeromes=int(input("Ingrese el mes que que quiere saber los accidentes"))-1
        i=0
        while len(self.__departamentos)>i:
            item=accidentes.buscar(i,numeromes)
            if (i + 1) == self.__departamentos[i].getnumero():
                print(f"En: {self.__departamentos[i].getnombre()} en el mes {numeromes + 1} ocurrieron {item} accidentes")
            i+=1
    
    def maximoaccidente(self,accidentes):
        numeromes=int(input("Ingrese el mes que quiere saber"))-1
        j=0
        band=False
        variable=accidentes.buscarmaximo(numeromes)
        cantidad=accidentes.buscar(variable,numeromes)
        while band is False and j<len(self.__departamentos):
            if variable + 1 == self.__departamentos[j].getnumero():
                print(f"En {self.__departamentos[j].getnombre()} ocurrieron {cantidad} de accidentes, y es el departamento que mas cantidentes tuvo en el mes de {numeromes + 1}")
            j+=1
    
    def totalaccidentesdepa(self,accidentes):
        departamentox=str(input("Ingrese el nombre de un departamento"))
        band=False
        numero=0
        i=0
        while band is False and i<len(self.__departamentos):
            if departamentox == self.__departamentos[i].getnombre():
                numero= self.__departamentos[i].getnumero() - 1 
                band= True
            i+=1
        cuenta=accidentes.contar(numero)
        print(f"La cantidad total de accidentes en {departamentox} es de {cuenta}")
                
        
        
            
            
        
        
                    
                
            
# if __name__=="__main__":
#     depa=ManejadorDepartamentos()
#     depa.cargarcsv()
#     depa.mostrardepartamentos()
    
        
    