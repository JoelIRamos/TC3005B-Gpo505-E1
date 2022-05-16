from pymongo import MongoClient

# Conexión a la base de datos
cluster = MongoClient("mongodb+srv://JoelIRamosH:JoelI@cluster0.htyzr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["TernData2"]