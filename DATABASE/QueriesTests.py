import pymongo
from pymongo import MongoClient
import json

cluster = MongoClient("mongodb+srv://JoelIRamosH:JoelI@cluster0.htyzr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["TernData2"]

## getHistoryList
# Obtiene todo el historial del sistema
## Parametro: nil 
def getHistoryList():
    collection = db["History"]
    results = list(collection.find({}))
    if len(results)>0:
        print(results)
        # data = {'message':'found', 'result': results}
        # data = {'message':'found', 'result': "a"}
    else:
        # data = {'message': 'Not found'}
        print("Not found")

#getHistoryList()

## getHistoryDetail/historyID
# De un historial en especifico se obtiene un archivo con todos sus atributos 
## Parametro: ID_Historial
def getHistoryDetail(historyID):
    collection = db["File"] # First, get all attributes
    fileResults = collection.find_one({"id_history": historyID})
    if len(fileResults) > 0:
        attr = fileResults["atribute"]
        #print(attr)
        ExtInt = db["History"].find_one({"_id": historyID}) # Second, get all internos y externos
        extern = ExtInt["externos"]
        intern = ExtInt["internos"]
        print({"attribute": attr, "externo": extern, "interno" : intern})
    


#getHistoryDetail(1)

def getLastSession(userID):
    collection = db["LastSession"]
    results = list(collection.find({"idUser": userID}))
    if len(results)>0:
        for result in results:
            historyID = result["idHistory"]
            print("History ID: " + str(historyID))
        # data = {'message':'found', 'result': results}
        # data = {'message':'found', 'result': "a"}
    else:
        # data = {'message': 'Not found'}
        print("Not found")

#getLastSession(0)

def deleteLastSession(userID):
    collection = db["LastSession"]
    collection.delete_one({"id_webUser": userID})

#deleteLastSession(1)

