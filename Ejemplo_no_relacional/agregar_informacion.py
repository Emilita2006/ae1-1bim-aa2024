"""
Agregar información en colecciones de MongoDB desde Python
"""
from enlace_base import client

# se obtiene la base de datos general
db = client.Base1

# colecciones específicas
coleccion_locales = db.locales_comida
coleccion_centros = db.centros_deportivos

# datos para la colección "locales_comida"
data_local_01 = {
    "nombre": "La Pizzeria",
    "direccion": "Calle Falsa 123",
    "tipo_cocina": "Italiana"
}

# agregar un solo documento a la colección "locales_comida"
coleccion_locales.insert_one(data_local_01)

# lista de documentos para la colección "locales_comida"
lista_locales = [
    {
        "nombre": "El Chifa",
        "direccion": "Av. Siempreviva 456",
        "tipo_cocina": "China"
    },
    {
        "nombre": "La Parrillada",
        "direccion": "Calle Luna 789",
        "tipo_cocina": "Ecuatoriana"
    }
]

# agregar múltiples documentos a la colección "locales_comida"
coleccion_locales.insert_many(lista_locales)

# datos para la colección "centros_deportivos"
data_centro_01 = {
    "nombre": "Polideportivo Central",
    "direccion": "Calle Sol 123",
    "tipo_deporte": "Fútbol"
}

# agregar un solo documento a la colección "centros_deportivos"
coleccion_centros.insert_one(data_centro_01)

# lista de documentos para la colección "centros_deportivos"
lista_centros = [
    {
        "nombre": "Gimnasio Olímpico",
        "direccion": "Av. Estrella 456",
        "tipo_deporte": "Baloncesto"
    },
    {
        "nombre": "Piscina Municipal",
        "direccion": "Calle Mar 789",
        "tipo_deporte": "Natación"
    }
]

# agregar múltiples documentos a la colección "centros_deportivos"
coleccion_centros.insert_many(lista_centros)
