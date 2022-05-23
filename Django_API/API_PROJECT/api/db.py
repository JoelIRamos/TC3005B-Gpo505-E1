from pymongo import MongoClient

# Conexión a la base de datos
cluster = MongoClient("localhost:27017")
db = cluster["TerniumData"]