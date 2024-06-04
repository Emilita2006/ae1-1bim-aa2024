"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)
db = client.Base1

coleccion_locales = db.locales_comida
coleccion_centros = db.centros_deportivos

# se usa método find_one, a partir de la colección
print("Muestra un solo documento de la colección 'locales_comida")
data_local_01 = coleccion_locales.find_one()
print(data_local_01)

# se usa método find, a partir de la colección
print("Muestra todos los documentos de la colección 'locales_comida'")
data_local_02 = coleccion_locales.find()
for registro in data_local_02:
    print(registro)
   
    # Consulta en la colección "centros_deportivos"
print("Muestra un solo documento de la colección 'centros_deportivos'")
data_centro_01 = coleccion_centros.find_one()
print(data_centro_01)

print("Muestra todos los documentos de la colección 'centros_deportivos'")
data_centro_02 = coleccion_centros.find()
for registro in data_centro_02:
    print(registro)
