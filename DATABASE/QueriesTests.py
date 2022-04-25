import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://JoelIRamosH:JoelI@cluster0.htyzr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["TernData"]

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
    FileCollection = db["File"]
    FileResults = list(FileCollection.find({"ID_History": historyID}))
    if len(FileResults)>0:
        for result in FileResults:
            FileID = result["_id"]
            print("File ID: " + str(FileID))
        # Obtain externo and interno attributes
        ExternoCollection = db["Externo"]
        ExternoResults = list(ExternoCollection.find({"ID_History": historyID}))
        InternoCollection = db["Interno"]
        InternoResults = list(InternoCollection.find({"ID_History": historyID}))
        ### FALTA OBTENER ATRIBUTOS EXT INT   
        ### FALTA 
        # Obtain all attributes from that file
        AttributeCollection = db["Attribute"]
        AttributeResults = list(AttributeCollection.find({"ID_File": FileID}))
        if len(AttributeResults)>0:
            for result in AttributeResults:
                print(result)
        else:
            print("No attributes")

        # data = {'message':'found', 'result': results}
        # data = {'message':'found', 'result': "a"}
    else:
        # data = {'message': 'Not found'}
        print("No file found")

getHistoryDetail(0)

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