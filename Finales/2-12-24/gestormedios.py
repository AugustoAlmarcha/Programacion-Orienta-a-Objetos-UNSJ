import csv
from Claseradio import Radio
from claseprensaescrita import PrensaEscrita
from clasemedio import Medio
from claseprograma import Programa
from datetime import datetime

class GestorMedios:
    __listamedios:list
    
    def __init__(self):
        self.__listamedios = []
        
    def agregarMedio(self, medio):
        self.__listamedios.append(medio)
        
    def cargarcsv(self):
        try:
            archivo=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Finales\2-12-24\Medios.csv")
            reader = csv.reader(archivo, delimiter=",")
            for fila in reader:
                if fila[0] == "R":
                    Radiox=Radio(fila[1],int(fila[2]),fila[3])
                    self.agregarMedio(Radiox)
                elif fila[0] == "P":
                    self.agregarMedio(PrensaEscrita(fila[1],int(fila[2]),fila[3],int(fila[4])))
        except Exception as e:
            print(e)
        except FileNotFoundError:
            print("El archivo no existe")
        try: 
            archivop=open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Finales\2-12-24\Programas.csv")
            readerprograma=csv.reader(archivop, delimiter=",")
            for filax in readerprograma:
                for medio in self.__listamedios:
                    if isinstance(medio,Radio):
                        band=medio.Eslafrecuencia(filax[0])
                        if band is True:
                            try:
                                medio.agregarprograma(Programa(filax[1].strip(), datetime.strptime(filax[2], "%H:%M").time(), datetime.strptime(filax[3], "%H:%M").time()))
                            except ValueError:
                                print(f"Formato de hora incorrecto en la fila: {filax}")
        except Exception as e:
            print(e)
        except FileNotFoundError:
            print("El archivo no existe")
            
    def mostrarMedios(self):
        for medio in self.__listamedios:
            if isinstance(medio,Radio):
                print("Radio")
            elif isinstance(medio,PrensaEscrita):
                print("Prensa Escrita")
            print(medio)
            print("----------------")
            
    def buscarPrograma(self,nombre):
        i=0
        band=False
        while i<len(self.__listamedios) and band is False:
            if isinstance(self.__listamedios[i],Radio):
                try:
                    self.__listamedios[i].programaexiste(nombre)
                    band=True
                except ValueError:
                    pass
            i+=1
        if band is False:
            raise ValueError
    
    def mostrarMediosespecificos(self):
        i=0
        while i< len(self.__listamedios):
            if isinstance(self.__listamedios[i],Radio):
                print("Radio")
            elif isinstance(self.__listamedios[i],PrensaEscrita):
                print("Prensa Escrita")
            print(f"Nombre : {self.__listamedios[i].get_nombre()}, Audiencia Estimada {self.__listamedios[i].get_audiencia()}, Indice de Audiencia {self.__listamedios[i].indice()}")
            i+=1
            
            
            
            
    
# if __name__=="__main__":
#     gestor= GestorMedios()
#     gestor.cargarcsv()
#     gestor.mostrarMedios()
            
            
                
                
        