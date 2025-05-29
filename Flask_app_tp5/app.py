#pip install flask
#pip install sqlalchemy
#pip install flask-sqlalchemy
#pip install flask-migrate
from flask import Flask,request,render_template,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from db import db
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_pyfile('config.py')
with app.app_context():
        db.init_app(app)

from modelo import Paquete, Sucursal, Repartidor, Transporte

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/sucursales')
def versucursales():
    sucursales = Sucursal.query.order_by(Sucursal.numero).all() #ordeno sucursales 
    return render_template("todassucursales.html", sucursales=sucursales) #query es un metodo para interactuar con la base de datos

@app.route('/operar', methods=['POST'])
def operar():
    if request.method == 'POST':  #Con el REQUEST se accede a los datos que el cliente envía al servidor
        sucursal_id = request.form.get('sucursale')  # Obtener el valor del campo 'sucursal' del formulario
        session['idSucursalElejida'] = int(sucursal_id)
        return redirect(url_for('opciones', sucursal_id=sucursal_id))

@app.route('/opciones/<int:sucursal_id>')    
def opciones(sucursal_id):
    return render_template('opciones.html', sucursal_id=sucursal_id)
#----------------------------------------------------------------------------------------------------
#FUNCIONALIDAD 2
@app.route('/registrar_paquete/<int:sucursal_id>', methods=['GET', 'POST']) #Cuando es una url manda un metodo get, get solicita y post envia datos
def registrar_paquete(sucursal_id):
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            nomdestinatario = request.form['nomdestinatario']
            dirdestinatario = request.form['dirdestinatario']
            
            numeroenvio = Paquete.query.count() + 1 # Generar automáticamente el número de envío
            
            nuevo_paquete = Paquete(numeroenvio=numeroenvio,
                                    peso=peso,
                                    nomdestinatario=nomdestinatario,
                                    dirdestinatario=dirdestinatario,
                                    idsucursal=sucursal_id,
                                    entregado=False)
            db.session.add(nuevo_paquete)
            db.session.commit()
            return render_template('registro_exitoso.html', numeroenvio=nuevo_paquete.numeroenvio)
        
        except Exception as e:
            error_msg = f"Error al registrar el paquete: {str(e)}"
            return render_template('error.html', error=error_msg)

    
    return render_template('registro_paquete.html', sucursal_id=sucursal_id) # Si es GET, muestra el formulario para registrar un nuevo paquete (siempre al principio va a ser get)
#--------------------------------------------------------------------------------
#FUNCIONALIDAD 3
@app.route("/salida_transporte/<int:sucursal_id>", methods=["GET", "POST"])
def salida_transporte(sucursal_id):
    if request.method == "POST":
        try:
            idsucursaldestino = int(request.form["idsucursaldestino"]) #Obtenemos los datos del formulario
            idpaquetes = request.form.getlist('idpaquetes')
            
            if not idpaquetes:
                error_msg = "Debes seleccionar al menos un paquete para el transporte."# Verificamos si se seleccionó al menos un paquete
                paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=0,idsucursal=sucursal_id).all()
                sucursales_destino = Sucursal.query.all()
                return render_template("salida_transporte.html", sucursales_destino=sucursales_destino, paquetes=paquetes, sucursal_id=sucursal_id)
            
            ultimo_transporte = Transporte.query.order_by(Transporte.numerotransporte.desc()).first() #descendente
            if ultimo_transporte:
                proximo_numero_transporte = ultimo_transporte.numerotransporte + 1
            else:
                proximo_numero_transporte = 1  # Si no hay transportes registrados, comenzamos desde el número 1
            
            nuevo_transporte = Transporte(idsucursal=idsucursaldestino, fechahorasalida=datetime.now(),numerotransporte=proximo_numero_transporte)
            db.session.add(nuevo_transporte)
            db.session.commit() #confirmar
    
            for idpaquete in idpaquetes:# Actualizamos los paquetes seleccionados con el nuevo transporte
                paquete = Paquete.query.get(int(idpaquete))
                if paquete:
                    paquete.idtransporte = nuevo_transporte.id  # Asociar el paquete con el nuevo transporte
                    paquete.idsucursal = sucursal_id  # Actualizar la sucursal de destino del paquete
                    db.session.commit()
                else:
                    error_msg = f"Paquete con id {idpaquete} no encontrado."
                    return render_template("error.html", error=error_msg)
            return render_template("exitoregistroenvio.html", numerotransporte=nuevo_transporte.numerotransporte)

        except Exception as e:
            error_msg = f"Error al registrar la salida del transporte: {str(e)}"
            return render_template("error.html", error=error_msg)
    else:
        sucursales_destino = Sucursal.query.all() # Obtener todas las sucursales para seleccionar la de destino
        paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=0,idsucursal=sucursal_id).all()
        
        return render_template("salida_transporte.html", sucursales_destino=sucursales_destino, paquetes=paquetes, sucursal_id=sucursal_id)
#-----------------------------------------------------------------------------------------------------------------------------
#FUNCIONALIDAD 4

@app.route("/llegada_transporte/<int:sucursal_id>", methods=["GET", "POST"])
def llega_transporte(sucursal_id):
    if request.method == "POST":
        try:
            transporte_id = int(request.form["transporte_id"])
            transporte = Transporte.query.get(transporte_id)
            if not transporte:
                error_msg = f"Transporte con ID {transporte_id} no encontrado."
                return render_template("error.html", error=error_msg)

            transporte.fechahorallegada = datetime.now()      # Registra la fecha y hora de llegada del transporte
            db.session.commit()
            return render_template("exitollegada.html", transporte=transporte)

        except Exception as e:
            error_msg = f"Error al registrar la llegada del transporte: {str(e)}"
            return render_template("error.html", error=error_msg)
    else:
        transportessinllegar = Transporte.query.filter_by(fechahorallegada=None,idsucursal=sucursal_id).all()
        return render_template('registrarllegadatransporte.html', transportessinllegar=transportessinllegar,sucursal_id=sucursal_id)
#-------------------------------------------------------------------------------------------------------------------------------------
@app.route('/repartidor')
def repartidor():
    return render_template("repartidores.html")








if __name__ == '__main__':
    app.run(debug=True)