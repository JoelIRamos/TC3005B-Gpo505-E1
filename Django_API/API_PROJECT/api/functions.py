# from typing_extensions import LiteralString
from typing import Collection
from unicodedata import category
from django.shortcuts import render
from django.http.response import JsonResponse

from django.views import View
import json

from api.db import db 
from bson.json_util import dumps
from bson.objectid import ObjectId
 
import pandas as pd
import numpy as np


def searchHistoryList(request): 
    # Buscar todos los registros de la coleccion "History" quitando las columnas "internos", "externos" y "graphs"
    runs = list(db["RunHistory"].find({}, {"internal_attributes": 0, "external__attributes": 0, "graphs": 0}))
    
    # Si hay registros regresarlos
    if len(runs)>0:
        # Lista con los archivos (resultado)
        result = []
        # Lista con los nombres de los archivos
        names = []
        
        # Para cada registro
        for run in runs:
            # Si el nombre del archivo no esta en la lista
            if run["base_file_name"] not in names:
                # Agregar a la lista de nombres
                names.append(run["base_file_name"])
        
        # Para cada nombre de archivo
        for name in names:
            # Crear el objeto con los datos del archivo
            file = {}
            file["base_file_name"] = name
            # Lista de las versiones de cada archivo
            file["versions"] = []
            
            # Para cada registro
            for run in runs:
                # Si el nombre del archivo es el mismo
                if run["base_file_name"] == name:
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


def searchHistoryDetail(request, historyID):
    # Buscar los registros de la coleccion "File" con el id_history e ignorar las columnas _id y id_history 
    fileResults = list(db["FileData"].find({"_id": historyID}, {'_id': 0, 'id_history': 0}))
    # Si hay registros regresarlos
    if len(fileResults) > 0:
        file = fileResults[0]["data"]
        # Buscar el registro de la coleccion "History" que tiene el historyID correspondiente
        ExtIntResults = db["RunHistory"].find_one({"_id": historyID})
        
        # Extraer los agentes externos, internos y la fecha
        external = ExtIntResults["external_attributes"]
        internal = ExtIntResults["internal_attributes"]
        date = ExtIntResults["date"]
        name = ExtIntResults["base_file_name"]
        try:
            graphs = ExtIntResults["graphs"]
        except:
            graphs = []
        # Formato de los Datos
        data = {
            'message':'found',
            'result': {
                'historyID': historyID,
                'base_file_name': name,
                'date': date,
                'internal_attributes': internal,
                'external_attributes': external,
                'graphs': graphs,
                'data': file
            }
        }
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)

def searchHistory(request, historyID):
    # Buscar el registro de la coleccion "History" que tiene el historyID correspondiente
    ExtIntResults = list(db["RunHistory"].find({"_id": historyID}))
    
    # Si hay sí existe el historyID
    if len(ExtIntResults) > 0:
        # Extraer el primer/unico registro
        ExtIntResult = ExtIntResults[0]
        
        # Extraer los agentes externos, internos y la fecha
        external = ExtIntResult["external_attributes"]
        internal = ExtIntResult["internal_attributes"]
        date = ExtIntResult["date"]
        name = ExtIntResult["base_file_name"]
        try:
            graphs = ExtIntResult["graphs"]
        except:
            graphs = []
        # Formato de los Datos
        data = {
            'message':'found',
            'result': {
                'historyID': historyID,
                'base_file_name': name,
                'date': date,
                'internal_attributes': internal,
                'external_attributes': external,
                'graphs': graphs
            }
        }
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)


# Función de ayuda para actualizar las graficas
async def updateGraphs(historyID, graph):
    # Usar coleccion "RunHistory"
    colection = db["RunHistory"]
    # Encontrar los registros que tienen el userID correspondiente (Maximo debe haber 1)
    results = list(colection.find({"_id": historyID}))
    
    # Si existe el registro
    if len(results)>0:
        # Usar la grafica del Body del request
        # graph = json.loads(request.body)
        try: 
            # Sacar las graficas actuales del registro
            graphs = results[0]["graphs"] 
            # Agregar la grafica al registro 
            graphs.append(graph)
        except:
            graphs = [graph]
        
        # Actualizar el registro
        colection.update_one({"_id": historyID}, {"$set": {"graphs": graphs}})
        # return {"message": "Success"}
        print("Success")
    else:
        print("updateGraphs: Not found")
        # return {'message': 'updateGraphs: Not found'}

# Barras, Linea helper
def searchBarLineGraphHelper(request, historyID, variable, filter, type):
    filter = float(filter)
    # Usar coleccion "FileData"
    colectionFD = db["FileData"]
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsFD = list(colectionFD.find({"_id": historyID}))
    # Si existe el historial
    if len(resultsFD) > 0:
        # Extraer los 'anomaly_socores' del registro
        anomaly_scores = resultsFD[0]["data"]["anomaly_scores"]
        anomalys = []
        
        # Llenar la lista de anomalias
        for i in range(len(anomaly_scores)):
            if (anomaly_scores[i] >= filter):
                anomalys.append(1)
            else: 
                anomalys.append(-1)
        
        # Crear data frame
        df =  pd.DataFrame({'atribute' :resultsFD[0]['data'][variable], 'anomaliy': anomalys})

        # Obtener total de anomalias
        anomalyTable = df.groupby(df.columns.tolist(),as_index=False).size()
        # print(anomalyTable)
        normalList = []
        anomalyList = []

        for i in range(len(anomalyTable)):
            if anomalyTable.iloc[i][1] == -1:
                categoryValue = anomalyTable.iloc[i][0]
                # Extraer el valor anterior
                try:
                    before = anomalyTable.iloc[i-1][0]
                except:
                    before = -1
                
                # Extraer el valor posterior
                try:
                    after = anomalyTable.iloc[i+1][0]
                except: 
                    after = -1
                
                # Verficar si el valor tiene una contraparte
                if (categoryValue != before) and (categoryValue != after):
                    normalList.append(0)
                
                anomalyList.append(anomalyTable.iloc[i][2])
            else:
                categoryValue = anomalyTable.iloc[i][0]
                # Extraer el valor anterior
                try:
                    before = anomalyTable.iloc[i-1][0]
                except:
                    before = -1
                
                # Extraer el valor posterior
                try:
                    after = anomalyTable.iloc[i+1][0]
                except: 
                    after = -1
                
                # Verficar si el valor tiene una contraparte
                if (categoryValue != before) and (categoryValue != after):
                    anomalyList.append(0)
                
                normalList.append(anomalyTable.iloc[i][2])
            
        # Crear data frame
        df =  pd.DataFrame({'anomalyList' : np.array(anomalyList), 'normalLists': np.array(normalList), 'atributeList': anomalyTable['atribute'].unique()})
        
        df = df.sort_values(by=['anomalyList'], ascending=False)

        # Solamente se envia el total de atributos y el total de anomalias de cada uno
        data = {
            'type': type,
            'labels': df['atributeList'].tolist(),
            'anomalyList': df['anomalyList'].tolist(),
            'normalList': df['normalLists'].tolist()
        }
        
        updateGraphs(historyID, data)
        
    else:
        data = { 'message': 'Not Found' }
    return JsonResponse(data)

def searchBarGraph(request, historyID, variable, filter):
    return searchBarLineGraphHelper(request, historyID, variable, filter, "Bar")

def searchLineGraph(request, historyID, variable, filter):
    return searchBarLineGraphHelper(request, historyID, variable, filter, "Line")

def searchBubbleGraph(request, historyID):
    return JsonResponse({'message': 'Not Implemented'})

def deleteGraph(request, historyID, graphID):
    # Usar la coleccion "RunHistory"
    collectionRH = db["RunHistory"]
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsRH = list(collectionRH.find({"_id": historyID}))
    # Si existe el historial
    if len(resultsRH) > 0:
        # Extraer la lista de graficas
        graphs = resultsRH[0]["graphs"]
        
        # Si el graphID esta fuera del alcance, mandar error
        if (graphID < 0 or graphID > len(graphs)-1):
            data = {'message': 'graphID Not Found'}
        else: 
            # Si no eliminar dicho elemento de la lista
            graphs.pop(graphID)
            
            # Actualizar el registro con la nueva lista
            collectionRH.update_one({"_id": historyID}, {"$set": {"graphs": graphs}})
            
            data = {'message': 'Success'}
    else:
        data = {'message': 'Not Found'}
    return JsonResponse(data)

def updateGraph(request, historyID, graphID):
    collection = db["FileData"]
    collection.delete_one({"_id": historyID})
    return JsonResponse({'message': 'Success'})

# * Pendientes: Documentacion, trigger y burbuja
'''
Terminar y Actualizar:
    Documento de Funcionalidades (Avanzado)
	Especificación de Requerimientos (Nuevos Requerimientos)
	Historias de Usuario (Nuevas Historias)
	Plan de Calidad (Pruebas)

Crear: 
	Bitacora de Pruebas (Nuevo)
	Manual de Usuario (Nuevo)
	Manual de Despliegue (Nuevo)

Terminados:
    Modelo de Calidad
    Documento Vision
    Plan de Comunicación
    Plan de Recursos
    Plan y Analisis de Riesgos

'''