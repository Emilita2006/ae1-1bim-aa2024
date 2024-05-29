from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
Base = declarative_base()

# Se crea la una entidad llamada Autor, que hereda
# de Base
class LocaldeComidas(Base):
    __tablename__ = 'LocaldeComidas' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombre = Column(String) # atributo de tipo String
    tipo_comida = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre, self.tipo_comida, self.direccion,
        self.telefono)

class CentroDeportivos(Base): 
    __tablename__ = 'CentroDeportivos' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreCentro = Column(String) # atributo de tipo String
    tipo_instalacion = Column(String)
    lugar = Column(String)
    contacto = Column(String)

    def __str__(self):
        return "%s %s %s %s" % (self.nombreCentro, self.tipo_instalacion, self.lugar,self.contacto)
# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)