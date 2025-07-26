class Libro:
    __titulo:str
    __autor:str
    __codigo:str
    __genero:str
    
    def __init__(self, titulo:str, autor:str, codigo:str, genero:str):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo
        self.__genero = genero
        
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_codigo(self):
        return self.__codigo
    
    def get_genero(self):
        return self.__genero
    
    def __str__(self):
        return f"Libro: {self.__titulo}, Autor: {self.__autor}, Código: {self.__codigo}, Género: {self.__genero}\n"