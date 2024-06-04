"""
Eliminar información en colecciones de MongoDB desde Python
"""
from enlace_base import client

# se obtiene la base de datos general
db = client.Base1

# colecciones específicas
coleccion_locales = db.locales_comida
coleccion_centros = db.centros_deportivos

# Mostrar todos los documentos de la colección 'locales_comida'
print("Muestra todos los documentos de la colección 'locales_comida'")
data_local_02 = coleccion_locales.find()
for registro in data_local_02:
    print(registro)

# Proceso para borrar documentos de la colección 'locales_comida' donde el tipo de cocina sea 'China'
print("Proceso para borrar documentos de la colección 'locales_comida' donde el tipo de cocina sea 'China'")
coleccion_locales.delete_many({'tipo_cocina': 'China'})

# Mostrar todos los documentos restantes de la colección 'locales_comida'
print("Muestra todos los documentos restantes de la colección 'locales_comida'")
data_local_02 = coleccion_locales.find()
for registro in data_local_02:
    print(registro)

# Mostrar todos los documentos de la colección 'centros_deportivos'
print("Muestra todos los documentos de la colección 'centros_deportivos'")
data_centro_02 = coleccion_centros.find()
for registro in data_centro_02:
    print(registro)

# Proceso para borrar documentos de la colección 'centros_deportivos' donde el tipo de deporte sea 'Fútbol'
print("Proceso para borrar documentos de la colección 'centros_deportivos' donde el tipo de deporte sea 'Fútbol'")
coleccion_centros.delete_many({'tipo_deporte': 'Fútbol'})

# Mostrar todos los documentos restantes de la colección 'centros_deportivos'
print("Muestra todos los documentos restantes de la colección 'centros_deportivos'")
data_centro_02 = coleccion_centros.find()
for registro in data_centro_02:
    print(registro)
