from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import winsound
from tkinter import Canvas
import json
from datetime import datetime
from tkinter import Menu
from gestor import *
class Simon:
    __lista=[] #almacena la secuencia generada por el juego
    __puntaje:int
    __record:int
    __contador:int
    __iniciado:bool
    __listacolores=[] #genera secuencias aleatorias
    
    def __init__(self):
        self.__ventana=Tk() #Creamos la ventana principal.
        self.__lista=[] 
        self.__puntaje=0 
        self.__record=0 
        self.__contador=0
        self.__iniciado=False
        self.__listacolores=["Azul", "Rojo", "Amarillo", "Verde"]
        self.__ventana.title("Simon")
        self.__ventana.geometry("400x500")
        self.__ventana.resizable(0,0)
        self.iniciarbotones()
        self.gestor_jugadores = GestorJugadores()
        self.crear_menu()
                  
    
    def iniciarbotones(self):
        self.__botonazul=Canvas(self.__ventana,height=200,width=180,bg="blue",bd=4,relief=RAISED)
        self.__botonazul.bind("<Button-1>",lambda event: self.presionar("Azul")) #Bind se utiliza para vincular eventos, 
        self.__botonazul.place(x=10,y=70)
        
        self.__botonrojo=Canvas(self.__ventana,height=200,width=180,bg="red",bd=4,relief=RAISED)
        self.__botonrojo.bind("<Button-1>",lambda event: self.presionar("Rojo"))
        self.__botonrojo.place(x=200,y=70)
        
        self.__botonamarrillo=Canvas(self.__ventana,height=200,width=180,bg="yellow",bd=4,relief=RAISED)
        self.__botonamarrillo.bind("<Button-1>",lambda event: self.presionar("Amarillo"))       
        self.__botonamarrillo.place(x=10,y=280)
        
        self.__botonverde=Canvas(self.__ventana,height=200,width=180,bg="green",bd=4,relief=RAISED)
        self.__botonverde.bind("<Button-1>",lambda event: self.presionar("Verde"))
        self.__botonverde.place(x=200,y=280)
        
        self.__botoniniciar=Canvas(self.__ventana, bg="white", height=50, width=120, bd=4, relief=RAISED) #bd (border width) para establecer un ancho de borde y relief para establecer el tipo de relieve.
        self.__botoniniciar.bind("<Button-1>", lambda event: self.ventananombre())
        self.__botoniniciar.create_text(50, 20, text="Ingresar Usuario", fill="black")
        self.__botoniniciar.place(x=240,y=10)
        
        self.__botonreintentar=Canvas(self.__ventana,bg="white",height=25,width=100,bd=4,relief=RAISED)
        self.__botonreintentar.bind("<Button-1>",lambda event: self.iniciar())
        self.__botonreintentar.create_text(50, 20, text="Reintentar", fill="black")
        self.__botonreintentar.place(x=10,y=0)
        
        self.__etiqueta=Label(self.__ventana,text="Puntaje: 0   Record: 0",bd=4,relief=RAISED)#Label se utiliza para mostrar texto
        self.__etiqueta.place(x=10,y=40)
    
    def ventananombre(self):
        self.ventanasecundaria = Toplevel(self.__ventana)
        self.ventanasecundaria.title("Juego Simon: Nombre:")
        self.ventanasecundaria.geometry("250x100")
        self.ventanasecundaria.resizable(0,0)
        
        self.etiquetanombre = Label(self.ventanasecundaria, text="Nombre:")
        self.etiquetanombre.grid(row=0, column=0, padx=5, pady=5)
        
        self.entrynombre = Entry(self.ventanasecundaria)
        self.entrynombre.grid(row=0, column=1, padx=5, pady=5)
        
        self.botonconfirmar = Button(self.ventanasecundaria, text="Confirmar", command=self.guardarnombre)
        self.botonconfirmar.grid(row=1, column=0, columnspan=2, pady=5) #determina cuántas columnas debería ocupar un widget en la cuadrícula
    
    def presionar(self, color):
        if self.__iniciado:
            if len(self.__lista) >= self.__contador - 1:
                if self.__lista[self.__contador] == color:
                    self.__contador += 1
                    self.turno()
                    self.__etiqueta.config(text=f"Jugador: {self.__nombrejugador} Puntaje: {self.__puntaje}  Record: {self.__record}")
                    self.cambio(color)
                else:
                    messagebox.showinfo("Game Over", f"Puntaje: {self.__puntaje}")
                    if self.__puntaje > self.__record:
                        self.__record = self.__puntaje
                    self.__etiqueta.config(text=f"Jugador: {self.__nombrejugador} Puntaje: {self.__puntaje}  Record: {self.__record}")
                    self.guardar_puntaje()
                    
                    self.__iniciado = False
                    self.__contador = 0
                    self.__puntaje = 0
                    self.__lista = []
    
    def guardarnombre(self):
        self.__nombrejugador = self.entrynombre.get()
        self.iniciar()  # Llama a iniciar después de guardar el nombre
                    
    def iniciar(self):
        self.__etiqueta.config(text=f"Jugador: {self.__nombrejugador} Puntaje: 0  Record: {self.__record}")
        self.ventanasecundaria.destroy()
        self.__contador=0
        self.__puntaje=0
        self.__lista=[]
        self.__iniciado=True
        self.__ventana.after(1500, self.crearcolor)
    
    def turno(self):
        if len(self.__lista)==self.__contador:
            self.__contador=0
            self.__puntaje+=1
            self.__ventana.after(1000,self.crearcolor)
    
    def crearcolor(self):
        if self.__iniciado:
            i = 0
            while i < len(self.__lista):
                self.cambio(self.__lista[i])
                i += 1
                self.__ventana.after(400)
                
            aleatorio = random.randrange(0, 4) #(start, stop-1)
            self.__lista.append(self.__listacolores[aleatorio])
            self.cambio(self.__lista[i])

    def cambio(self, color):
        canvas = self.getcolorcanvas(color) #obtiene el boton
        color_original = self.get_color_rgb(canvas) #obtiene una cadena que representa el color de fondo actual
        color_cambio = self.get_color_cambio(color)
        canvas.configure(bg=color_cambio)
        self.__ventana.update()
        self.sonido(color)
        canvas.configure(bg=color_original)
        self.__ventana.update()#forzar a la ventana principal para que procese todos los eventos pendientes en la cola de eventos de Tkinter. 
    #Después de cada interacción del jugador, el programa vuelve a esperar el siguiente clic del jugador para continuar con el juego.
    def sonido(self, color):
        if color == "Azul":
            winsound.Beep(500, 500)
        elif color == "Rojo":
            winsound.Beep(700, 500)
        elif color == "Amarillo":
            winsound.Beep(600, 500)
        elif color == "Verde":
            winsound.Beep(800, 500)

    def getcolorcanvas(self, color):
        if color == "Azul":
            return self.__botonazul
        elif color == "Rojo":
            return self.__botonrojo
        elif color == "Amarillo":
            return self.__botonamarrillo
        elif color == "Verde":
            return self.__botonverde

    def get_color_rgb(self, canvas):
        return canvas["bg"] #accedo al valor actual del atributo bg

    def get_color_cambio(self, color):
        if color == "Azul":
            return "#6A5ACD"
        elif color == "Rojo":
            return "#800000"
        elif color == "Amarillo":
            return "orange"
        elif color == "Verde":
            return "#00FF00"
     
    def guardar_puntaje(self):
        puntaje_data = {
            "Jugador": self.__nombrejugador,
            "Fecha": datetime.now().strftime("%Y-%m-%d"),  #Creo un diccionario  
            "Hora": datetime.now().strftime("%H:%M:%S"), #Al almacenar fechas y horas en estos formatos estandarizados, facilitas la posterior manipulación, búsqueda y presentación de estos datos
            "Puntaje": self.__puntaje
        }
        json_path = r"C:\Users\Usuario\Desktop\Tkinter oficial\pysimonpuntajes.json"   #Modificar aca
        with open(json_path, "a") as file: #PATH = RUTA 
            json.dump(puntaje_data, file) #"a"= para añadir al final del archivo.
            file.write('\n')
    
    def crear_menu(self):
        menu = Menu(self.__ventana)
        self.__ventana.config(menu=menu)
        opciones_menu = Menu(menu)
        menu.add_cascade(label="Opciones", menu=opciones_menu)
        opciones_menu.add_command(label="Ver puntajes", command=self.ver_puntajes)
        opciones_menu.add_command(label="Salir", command=self.salir)

    def ver_puntajes(self):
        json_path = r"C:\Users\Usuario\Desktop\Tkinter oficial\pysimonpuntajes.json" #Modificar aca
        self.gestor_jugadores.cargardesdejson(json_path)
        self.gestor_jugadores.ordenar_jugadores()

        puntajes_str = ""
        for jugador in self.gestor_jugadores.getjugadores():
            puntajes_str += f"Nombre: {jugador.getNombre()}, Puntaje: {jugador.getPuntaje()}, Fecha: {jugador.getFecha()}, Hora: {jugador.getHora()}\n"
        messagebox.showinfo("Puntajes", puntajes_str)

    def salir(self):
        self.__ventana.quit()     
            
    def run(self):
        self.__ventana.mainloop()
    

algo=Simon()
algo.run()