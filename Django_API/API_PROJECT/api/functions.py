from django.shortcuts import render
from django.http.response import JsonResponse

from django.views import View
import json

from api.db import db 
from bson.json_util import dumps
from bson.objectid import ObjectId


def searchOption1(request):
    # Buscar todos los registros de la coleccion "History" quitando las columnas "internos", "externos" y "graphs"
    results = list(db["RunHistory"].find({}, {"internos": 0, "externos": 0, "graphs": 0}))
    
    # Si hay registros regresarlos
    if len(results)>0:
        data = {'message':'found', 'result': results}
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)

def searchOption2(request):
    # Buscar todos los registros de la coleccion "History" quitando las columnas "internos", "externos" y "graphs"
    runs = list(db["RunHistory"].find({}, {"internos": 0, "externos": 0, "graphs": 0}))
    
    # Si hay registros regresarlos
    if len(runs)>0:
        # Lista con los archivos (resultado)
        result = []
        # Lista con los nombres de los archivos
        names = []
        
        # Para cada registro
        for run in runs:
            # Si el nombre del archivo no esta en la lista
            if run["name"] not in names:
                # Agregar a la lista de nombres
                names.append(run["name"])
        
        # Para cada nombre de archivo
        for name in names:
            # Crear el objeto con los datos del archivo
            file = {}
            file["name"] = name
            # Lista de las versiones de cada archivo
            file["versions"] = []
            
            # Para cada registro
            for run in runs:
                # Si el nombre del archivo es el mismo
                if run["name"] == name:
                    # Objeto con el id y la fecha de la version
                    version = {
                        "_id": run["_id"],
                        "date": run["date"],
                    }
                    # Agregar la version
                    file["versions"].append(version)
            
            # Agregar el archivo a la lista de resultados
            result.append(file)
        
        # Crear el objeto con los resultados
        data = { "message": "found", "result": result }
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)

def searchHistoryList(request): 
    return searchOption2(request)

def searchUserID(request, historyID):
    # Usar coleccion "LastSession"
    colectionLS = db["LastSession"]
    # Buscar si hay registros que tienen el historyID correspondiente (Maximo debe haber 1)
    lSresults = list(colectionLS.find({"id_history": historyID}))
    
    # Verificar que no exista un registro con el historyID en la coleccion de LastSession
    if len(lSresults)>0:
        data = {'message': 'session already in use'}
    else: 
        # Verificar si existe un registro con el historyID en la coleccion de History
        rHresult = list(db["RunHistory"].find({"_id": historyID}))
        if (len(rHresult)>0):
            # Insertar el historyID en la coleccion de LastSession (esto crea automaticamente un userID)
            colectionLS.insert_one({"id_history": historyID})
            # Obtener dicho registro para obtener el userID
            newRegister = colectionLS.find_one({"id_history": historyID})
            
            # Regresar el userID
            data = {'message': 'success', 'userID': str(newRegister['_id'])}
        else :
            data = {'message': 'historyID unexistent'}
    
    return JsonResponse(data)


def searchHistoryDetailHelper(request, historyID):
    # Buscar los registros de la coleccion "File" con el id_history e ignorar las columnas _id y id_history 
    fileResults = list(db["FileData"].find({"id_history": historyID}, {'_id': 0, 'id_history': 0}))
    # Si hay registros regresarlos
    if len(fileResults) > 0:
        file = fileResults[0]["file"]
        # Buscar el registro de la coleccion "History" que tiene el historyID correspondiente
        ExtIntResults = db["RunHistory"].find_one({"_id": historyID})
        
        # Extraer los agentes externos, internos y la fecha
        extern = ExtIntResults["externos"]
        intern = ExtIntResults["internos"]
        date = ExtIntResults["date"]
        name = ExtIntResults["name"]
        try:
            graphs = ExtIntResults["graphs"]
        except:
            graphs = []
        # Formato de los Datos
        data = {
            'message':'found',
            'result': {
                'historyID': historyID,
                'name': name,
                'date': date,
                'interno': intern,
                'externo': extern,
                'graphs': graphs,
                'file': file
            }
        }
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return data


def searchHistoryDetail(request, historyID):
    return JsonResponse(searchHistoryDetailHelper(request, historyID))


def searchLastSession(request, userID):
    try: 
        # Hacer el objectid del userID
        objUserID = ObjectId(userID)
    except: 
        return JsonResponse({'message': 'userID is not a valid ObjectID'})
    
    # Usar coleccion "LastSession"
    colectionLS = db["LastSession"]
    # Encontrar los registros que tienen el userID correspondiente (Maximo debe haber 1)
    lSresults = list(colectionLS.find({"_id": objUserID}))
    
    # Si existe el registro regresar los datos
    if len(lSresults)>0:
        # Extraer el histortID
        historyID = lSresults[0]["id_history"]
        
        # Hacer la busqueda de la tabla con dicho historyID
        data = searchHistoryDetailHelper(request, historyID)
        
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'Not found'})

# * Recordar Hacer trigger de timer en MongoDB
def deleteLastSession(request, userID):
    try: 
        # Hacer el objectid del userID
        objUserID = ObjectId(userID)
        # Usar coleccion "LastSession"
        collection = db["LastSession"]
        # Buscar la lista de los registros que tienen el userID correspondiente (Maximo debe haber 1)
        result = list(collection.find({"_id": objUserID}))
        
        # Si existe el registro borrarlo
        if len(result)>0:
            # Eliminar el registro
            collection.delete_one({"_id": objUserID})
            # Regresar mensaje de exito
            data = {'message': 'Success'}
            
        else: # Si no existe el registro regresar mensaje de error
            data = {'message': 'Not found'}
    except:
        data = { 'message': 'userID is not a valid ObjectID' }
    return JsonResponse(data)


# ToDo: Cambiar Totalmente
def updateHistory(request, userID):
    # Hacer el objectid del userID
    objUserID = ObjectId(userID) 
    # Usar coleccion "LastSession"
    colectionLS = db["LastSession"]
    # Encontrar los registros que tienen el userID correspondiente (Maximo debe haber 1)
    lSresults = list(colectionLS.find({"_id": objUserID}))
    
    # Si existe el registro regresar los datos
    if len(lSresults)>0:
        # Extraer el histortID
        historyID = lSresults[0]["id_history"]
        # Extraer las graficas del request
        graphs = json.loads(request.body)
        
        # Usar la coleccion "History"
        colectionH = db["RunHistory"]
        
        # Hacer update a la tabla con dicho historyID
        colectionH.update_one({"_id": historyID}, {"$set": {"graphs": graphs}})
        
        return JsonResponse({"message": "Success"})
    else:
        return JsonResponse({'message': 'Not found'})


# * Pendientes: gets Asyncornos, Cambiar Documentacion & Junta con frontend
# Barras, Aeras, Burbujas