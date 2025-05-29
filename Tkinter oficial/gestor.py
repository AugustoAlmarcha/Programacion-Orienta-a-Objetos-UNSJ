from jugador import *
import json
class GestorJugadores:
    __jugadores=[]
    def __init__(self):
        self.__jugadores = []
    
    def agregar_jugador(self, jugador):
        self.__jugadores.append(jugador)
    
    def ordenar_jugadores(self):
        self.__jugadores.sort(reverse=True)
    
    def cargardesdejson(self, json_path):
        self.__jugadores.clear()
        json_path = r"C:\Users\Usuario\Desktop\Tkinter oficial\pysimonpuntajes.json" #Modificar aca
        try:
            with open(json_path, "r") as file:
                for linea in file:
                    datos = json.loads(linea.strip()) #STRIP es un método de las cadenas en Python que elimina los caracteres en blanco, LOADS convierte esa línea en un diccionario
                    jugador = Jugador(datos["Jugador"], datos["Puntaje"], datos["Fecha"], datos["Hora"])
                    self.agregar_jugador(jugador)
        except FileNotFoundError:
            print(f"El archivo {json_path} no existe.")
    
    def getjugadores(self):
        return self.__jugadores