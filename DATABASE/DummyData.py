import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://JoelIRamosH:JoelI@cluster0.htyzr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["TernData"]
collectionLastSe = db["LastSession"]

############### Last Session
LastSessionData = [
  {"_id": 0, "idHistory": 0, "idUser": 0},
  {"_id": 1, "idHistory": 1, "idUser": 1},
  {"_id": 2, "idHistory": 2, "idUser": 2},
  {"_id": 3, "idHistory": 3, "idUser": 3},
  {"_id": 4, "idHistory": 4, "idUser": 4}
]

collectionLastSe.insert_many(LastSessionData)

############## History

collectionHistory = db["History"]
HistoryData = [
  {"_id": 0,  "Date": "2022-5-15"},
  {"_id": 1,  "Date": "2022-5-18"},
  {"_id": 2,  "Date": "2022-5-26"},
  {"_id": 3,  "Date": "2022-6-16"},
  {"_id": 4,  "Date": "2022-5-18"},
  {"_id": 5,  "Date": "2022-5-20"},
  {"_id": 6,  "Date": "2022-5-25"},
  {"_id": 7,  "Date": "2022-5-29"},
  {"_id": 8,  "Date": "2022-6-2"},
  {"_id": 9,  "Date": "2022-5-1"}
]

collectionHistory.insert_many(HistoryData)

############### Externo
collectionExterno = db["Externo"]
ExternoData = [
  {"_id": 0,  "ID_History": 0, "ID_Attribute": 0},
  {"_id": 1,  "ID_History": 1, "ID_Attribute": 1},
  {"_id": 2,  "ID_History": 2, "ID_Attribute": 2},
  {"_id": 3,  "ID_History": 3, "ID_Attribute": 3},
  {"_id": 4,  "ID_History": 4, "ID_Attribute": 4}
]
collectionExterno.insert_many(ExternoData)

############### Interno
collectionInterno = db["Interno"]
InternoData = [
  {"_id": 0,  "ID_History": 5, "ID_Attribute": 5},
  {"_id": 1,  "ID_History": 6, "ID_Attribute": 6},
  {"_id": 2,  "ID_History": 7, "ID_Attribute": 7},
  {"_id": 3,  "ID_History": 8, "ID_Attribute": 8},
  {"_id": 4,  "ID_History": 9, "ID_Attribute": 9}
]
collectionInterno.insert_many(InternoData)

############### File
collectionFile = db["File"]
FileData = [
  {"_id": 0,  "ID_History": 0},
  {"_id": 1,  "ID_History": 1},
  {"_id": 2,  "ID_History": 2},
  {"_id": 3,  "ID_History": 3},
  {"_id": 4,  "ID_History": 4}
]
collectionFile.insert_many(FileData)

############### Attribute
collectionAttribute = db["Attribute"]
AttributeData = [
  {"_id": 0,  "ID_File": 0, "C_Sociedad": "TM01"},
  {"_id": 1,  "ID_File": 0, "ID_TRASNPORTISTA": 1001},
  {"_id": 2,  "ID_File": 0, "TRACTOR": "88AH7U"},
  {"_id": 3,  "ID_File": 0, "D_PATENTE": "344VU5"},
  {"_id": 4,  "ID_File": 0, "Q_CANTIDAD": 33},
  {"_id": 5,  "ID_File": 0, "weightDifference": -0.95},
  {"_id": 6,  "ID_File": 0, "ID_PROVEEDOR": 12345566},
  {"_id": 7,  "ID_File": 0, "N_PESO_TA": 21.12},
  {"_id": 8,  "ID_File": 0, "mediana": 16.62},
  {"_id": 9,  "ID_File": 0, "PesoDiffer": 4.5},
]
collectionAttribute.insert_many(AttributeData)


