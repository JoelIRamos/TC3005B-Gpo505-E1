from django.shortcuts import render
from django.http.response import JsonResponse

from django.views import View
import json

from api.db import db 
from bson.json_util import dumps

def searchHistoryList(request):
    collection = db["History"]
    results = list(collection.find({}))
    if len(results)>0:
        data = {'message':'found', 'result': results}
    else:
        data = {'message': 'Not found'}
    return JsonResponse(data)

def searchHistoryDetail(request, historyID):
    collection = db["File"] # First get all files
    fileResults = collection.find_one({"id_history": historyID})
    if len(fileResults) > 0:
        attr = fileResults["attribute"]
        
        #ToDo: Mejorar formato de respuesta
        ExtInt = db["History"].find_one({"_id": historyID}) # ! Quitar el find One
        extern = ExtInt["externos"]
        intern = ExtInt["internos"]
        date = ExtInt["date"]
        data = {'message':'found', 'attribute': attr, 
                'interno': intern, 'externo': extern, 'date': date}
    else:
        data = {'message': 'Not found'}
    return JsonResponse(data)


def searchLastSession(request, userID):
    # Informacion de la sesion
    collectionLS = db["LastSession"]
    lSresults = collectionLS.find_one({"id_webUser": userID})
    if len(lSresults)>0:
        # Informacion del archivo
        historyID = lSresults["id_history"]
        collectionFile = db["File"]
        
        # ToDo: Mejorar formato de respuesta
        fileResults = list(collectionFile.find({"id_history": historyID}, {'_id': 0, 'id_history': 0}))
        data = {'message':'found', 'result': lSresults, 'file': fileResults}
    else:
        data = {'message': 'Not found'}
    return JsonResponse(data)


def deleteLastSession(request, userID):
    collection = db["LastSession"]
    result = list(collection.find({"_id": userID})) # * Debe ser find y list, no find_one 
    if len(result)>0:
        collection.delete_one({"_id": userID})
        data = {'message': 'Success'}
    else:
        data = {'message': 'Not found'}
    return JsonResponse(data)

# ToDo: Implementar la funcion del metodo POST
# ! Quedar en el estandar de almacenamiento de graficas
def insertLastSession(request, userID, historyID):
    return JsonResponse({'message': 'endpoint not implemented, funtion not implemented'})


# ToDo: Implementar la funcion del metodo PUT
def updateLastSession(request, userID):
    # ! Quedar en el estandar para almacenar las graficas
    return JsonResponse({'message': 'endpoint not implemented, funtion not implemented'})

# ToDo: Implementar la funcion del metodo POST
def insertToHistory(request, userID):
    # ! La subida de archivo todavia está en prueba
    return JsonResponse({'message': 'endpoint not implemented, funtion not implemented'})