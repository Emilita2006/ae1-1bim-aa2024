from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import LocaldeComidas,CentroDeportivos
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()
# Se crean objetos de tipo LocaldeComidas
local1 = LocaldeComidas(nombre="Restaurante El Buen Sabor", tipo_comida="Comida mexicana", direccion="Calle Principal 123", telefono="123456789")
local2 = LocaldeComidas(nombre="Pizzería La Italiana", tipo_comida="Pizza", direccion="Avenida Central 456", telefono="987654321")

# Se crean objetos de tipo CentroDeportivo
centro1 = CentroDeportivos(nombreCentro="Gimnasio Fitness Plus", tipo_instalacion="Gimnasio", lugar="Plaza Deportiva 789", contacto="456123789")
centro2 = CentroDeportivos(nombreCentro="Complejo Deportivo Los Robles", tipo_instalacion="Complejo Deportivo", lugar="Calle Deportiva 321", contacto="789456123")

# a la espera de un commit
session.add(local1)
session.add(local2)
session.add(centro1)
session.add(centro2)
# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
