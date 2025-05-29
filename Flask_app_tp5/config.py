
SECRET_KEY = "GDtfDCFYjD"   #Esta variable SECRET_KEY se utiliza en Flask para proteger tu aplicación contra ataques CSRF 

SQLALCHEMY_DATABASE_URI = 'sqlite:///C:/Users/Usuario/Desktop/Python/Flask_app_tp5/datos.sqlite3'  
#Esta configuración SQLALCHEMY_DATABASE_URI especifica la ubicación de la base de datos

SQLALCHEMY_TRACK_MODIFICATIONS = False 
#Esta configuración controla si SQLAlchemy debe rastrear las modificaciones en los objetos y enviar señales para la aplicación Flask cada vez que se modifica un objeto.