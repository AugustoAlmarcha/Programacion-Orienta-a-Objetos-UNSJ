from clasematerialrefractario import MaterialRefractario
import csv
from random import randint

class ClaseGestorMaterial:
    __listamaterial: list

    def __init__(self):
        self.__listamaterial = []

    def agregarMaterial(self, material: MaterialRefractario):
        self.__listamaterial.append(material)
        
    def cargarcsv(self):
        try: 
            archivo = open(r"Ejercicios 2da chance/Unidad 3/Ejercicio 2/materiales.csv")
            reader = csv.reader(archivo, delimiter=';')
            next(reader)  
            for fila in reader:
                self.agregarMaterial(MaterialRefractario(int(fila[0]), fila[1], float(fila[2]), float(fila[3])))
            archivo.close()
        except FileNotFoundError:
            print("El archivo no se encuentra en la ruta especificada.")
        except Exception as e:
            print(f"Se produjo un error al cargar el archivo: {e}")
    
    def mostrarmaterial(self):
        for material in self.__listamaterial:
            print(material)
    
    def get_material_random(self):
        if self.__listamaterial:
            return self.__listamaterial[randint(0, len(self.__listamaterial)-1)]
        return None
    

            
# if __name__ == "__main__":
#     gestor = ClaseGestorMaterial()
#     gestor.cargarcsv()
#     gestor.mostrarmaterial()
    
    

