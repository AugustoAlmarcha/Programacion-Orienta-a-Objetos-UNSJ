from claseruta import *
import csv

class gestorruta:
    __listaruta:list
    
    def __init__(self):
        self.__listaruta = []
        
    def agregarruta(self,ruta):
        self.__listaruta.append(ruta)
    
    def cargarcsv(self):
        try:
            archivo = open(r"C:\Users\Usuario\Desktop\Estudio para final poo\Ejercicios 2da chance\Finales\16-12-24\Rutas.csv")
            reader = csv.reader(archivo, delimiter = ';')
            next(reader)
            for fila in reader:
                asignada = fila[3].strip().upper() == "VERDADERO"
                self.agregarruta(Ruta(int(fila[0]), fila[1], float(fila[2].replace(",", ".")), asignada))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as e:
            print(f"Error: {e}")
            
    def mostrar(self):
        for ruta in self.__listaruta:
            print(ruta)
    
    def asignarruta(self,camion,codigo):
        i=0
        band=False
        while i<len(self.__listaruta) and not band:
            if self.__listaruta[i].get_codigo()==codigo:
                if self.__listaruta[i].get_rutaasignada():
                    raise IOError
                else:
                    camion.agregarruta(self.__listaruta[i])
                    band=True
            i+=1
        if band is True:
            print("Ruta asignada correctamente")
            self.__listaruta[i-1].set_asignada(True)
        else:
            raise IndexError
                
            
# if __name__ == "__main__":
#     ruta = gestorruta()
#     ruta.cargarcsv()
#     ruta.mostrar()
    
    