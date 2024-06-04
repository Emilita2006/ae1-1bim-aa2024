"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.ejemploMongo001
db = client.Base1

# colecciones específicas
coleccion_locales = db.locales_comida
coleccion_centros = db.centros_deportivos

# Consulta en la colección "locales_comida"
print("Muestra un solo documento de la colección 'locales_comida' con nombre 'La Pizzeria'")
data_local_01 = coleccion_locales.find_one({'nombre': 'La Pizzeria'})
print(data_local_01)

print("Muestra todos los documentos de la colección 'locales_comida' que tengan tipo de cocina 'China'")
data_local_02 = coleccion_locales.find({'tipo_cocina': 'China'})
for registro in data_local_02:
    print(registro)

# Consulta en la colección "centros_deportivos"
print("Muestra un solo documento de la colección 'centros_deportivos' con nombre 'Polideportivo Central'")
data_centro_01 = coleccion_centros.find_one({'nombre': 'Polideportivo Central'})
print(data_centro_01)

print("Muestra todos los documentos de la colección 'centros_deportivos' que tengan tipo de deporte 'Fútbol'")
data_centro_02 = coleccion_centros.find({'tipo_deporte': 'Fútbol'})
for registro in data_centro_02:
    print(registro)
