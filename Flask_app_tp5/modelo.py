from db import db
from datetime import datetime

class Paquete(db.Model):
    __tablename__ = "paquete" #especifica el nombre de la tabla en la base de datos que está representando esa clase
    
    id = db.Column(db.Integer, primary_key = True)
    numeroenvio = db.Column(db.Integer)
    peso = db.Column(db.Float)
    nomdestinatario = db.Column(db.String(150))
    dirdestinatario = db.Column(db.String(150))
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.String(150), default="")
    #---------------------------------------------------------------------
    idsucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    sucursal = db.relationship("Sucursal", back_populates="paquetes") #back_populates se utiliza para especificar el nombre del atributo en la clase relacionada que representa la relación inversa.
    idtransporte = db.Column(db.Integer, db.ForeignKey("transporte.id"), default=0 )
    transporte = db.relationship("Transporte", back_populates="paquetes")
    idrepartidor = db.Column(db.Integer, db.ForeignKey("repartidor.id"), default=0)
    repartidor = db.relationship("Repartidor", back_populates="paquetes")
    
class Sucursal(db.Model):
    __tablename__ = "sucursal"

    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer)
    provincia = db.Column(db.String(150))
    localidad = db.Column(db.String(150))
    direccion = db.Column(db.String(150))
    #--------------------------------------------------------------------------------------------
    paquetes = db.relationship("Paquete", back_populates="sucursal", cascade="all, delete-orphan")
    transportes = db.relationship("Transporte", back_populates="sucursal", cascade="all, delete-orphan")
    repartidores = db.relationship("Repartidor", back_populates="sucursal", cascade="all, delete-orphan")


class Repartidor(db.Model):
    __tablename__ = "repartidor"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(150))
    dni = db.Column(db.String(20))
    #---------------------------------------------------------------------------------------------------------------
    idsucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    sucursal = db.relationship("Sucursal", back_populates="repartidores", single_parent=True, cascade="all, delete-orphan")
    paquetes = db.relationship("Paquete", back_populates="repartidor", cascade="all, delete-orphan")


class Transporte(db.Model):
    __tablename__ = "transporte"

    id = db.Column(db.Integer, primary_key = True)
    numerotransporte = db.Column(db.Integer)
    fechahorasalida = db.Column(db.DateTime, default=datetime.now())
    fechahorallegada = db.Column(db.DateTime, default=None)
    #---------------------------------------------------------------------------------------------------------------------
    idsucursal = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    sucursal = db.relationship("Sucursal", back_populates="transportes", single_parent=True, cascade="all, delete-orphan")
    paquetes = db.relationship("Paquete", back_populates="transporte", cascade="all, delete-orphan")
