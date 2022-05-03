from django.shortcuts import render
from django.http.response import JsonResponse

from django.views import View
import json

from api.db import db 
from bson.json_util import dumps



def searchHistoryList(request): 
    # Buscar todos los registros de la coleccion "History"
    results = list(db["History"].find({}))
    
    # Si hay registros regresarlos
    if len(results)>0:
        data = {'message':'found', 'result': results}
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)


def searchHistoryDetailHelper(request, historyID):
    # Buscar los registros de la coleccion "File" con el id_history e ignorar las columnas _id y id_history 
    fileResults = list(db["File"].find({"id_history": historyID}, {'_id': 0, 'id_history': 0}))
    # Si hay registros regresarlos
    if len(fileResults) > 0:
        # Buscar el registro de la coleccion "History" que tiene el historyID correspondiente
        collectionExtInt = db["History"].find_one({"_id": historyID})
        
        # Filtrar por los campos que se quieren regresar # ! O(n): buscar una mejor forma de hacerlo
        file = []
        for row in fileResults:
            file.append(row['attribute'])
        
        # Extraer los agentes externos, internos y la fecha
        extern = collectionExtInt["externos"]
        intern = collectionExtInt["internos"]
        date = collectionExtInt["date"]
        graphs = collectionExtInt["graphs"]
        # Formato de los Datos
        data = {
            'message':'found',
            'result': {
                'historyID': historyID,
                'date': date,
                'interno': intern,
                'externo': extern,
                'graphs': graphs,
                'file': file
                # 'attribute': fileResults 
            }
        }
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return data


def searchHistoryDetail(request, historyID):
    return JsonResponse(searchHistoryDetailHelper(request, historyID))


def searchLastSession(request, userID):
    # Usar coleccion "LastSession"
    colectionLS = db["LastSession"]
    # Encontrar los registros que tienen el userID correspondiente (Maximo debe haber 1)
    lSresults = list(colectionLS.find({"id_webUser": userID}))
    
    # Si existe el registro regresar los datos
    if len(lSresults)>0:
        # Extraer el histortID
        historyID = lSresults[0]["id_history"]
        
        # Hacer la busqueda de la tabla con dicho historyID
        data = searchHistoryDetailHelper(request, historyID)
        
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'Not found'})


# * ESTE SE MANDA LLAMAR CUANDO EL USUARIO SE DESLOGUEA
def deleteLastSession(request, userID):
    # Usar coleccion "LastSession"
    collection = db["LastSession"]
    # Buscar la lista de los registros que tienen el userID correspondiente (Maximo debe haber 1)
    result = list(collection.find({"id_webUser": userID}))
    
    # Si existe el registro borrarlo
    if len(result)>0:
        # Eliminar el registro
        collection.delete_one({"id_webUser": userID})
        # Regresar mensaje de exito
        data = {'message': 'Success'}
        
    else: # Si no existe el registro regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)


def updateHistory(request, userID): 
    # Usar coleccion "LastSession"
    colectionLS = db["LastSession"]
    # Encontrar los registros que tienen el userID correspondiente (Maximo debe haber 1)
    lSresults = list(colectionLS.find({"id_webUser": userID}))
    
    # Si existe el registro regresar los datos
    if len(lSresults)>0:
        # Extraer el histortID
        historyID = lSresults[0]["id_history"]
        # Extraer las graficas del request
        graphs = json.loads(request.body)
        
        # Usar la coleccion "History"
        colectionH = db["History"]
        
        # Hacer update a la tabla con dicho historyID
        colectionH.update_one({"_id": historyID}, {"$set": {"graphs": graphs}})
        
        # print(historyID)
        # print(graphs)
        
        return JsonResponse({"message": "Success"})
    else:
        return JsonResponse({'message': 'Not found'})


# TODO: CAMBIAR A GETUSERID LO CUAL CREA EL LAST SESSION
def insertLastSession(request, userID, historyID):
    # TODO: CAMBIAR PARA QUE SE CREE UN USERID DE ACUERDO A UN HISTORYID
    return JsonResponse({'message': 'endpoint not implemented, funtion not implemented'})


# ToDo: Implementar la funcion del metodo POST
def insertToHistory(request, userID):
    # ! La subida de archivo todavia está en prueba
    return JsonResponse({'message': 'endpoint not implemented, funtion not implemented'})

# * Pendientes: Hacer los Cambios Aqui, Cambiar en mongoDB Graphs, Cambiar Documentacion & Junta con frontend