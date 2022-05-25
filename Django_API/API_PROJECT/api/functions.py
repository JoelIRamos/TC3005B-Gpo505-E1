# from typing_extensions import LiteralString
from cProfile import label
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
        informational = ExtIntResults["informational_attributes"]
        
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
                'informational_attributes': informational,
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
        informational = ExtIntResult["informational_attributes"]
        
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
                'informational_attributes': informational,
                'graphs': graphs
            }
        }
        
    else: # Si no hay registros regresar mensaje de error
        data = {'message': 'Not found'}
    return JsonResponse(data)


# Barras, Linea helper
def searchBarLineGraphHelper(request, historyID, variable, filter, type):
    filter = float(filter)
    # Usar coleccion "FileData"
    colectionFD = db["FileData"]
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsFD = list(colectionFD.find({"_id": historyID}, {"data." + variable : 1, "data.anomaly_scores": 1}))
    
    # Si existe el historial
    if len(resultsFD) > 0:
        # Crear data frame
        originalDf =  pd.DataFrame({'attribute' :resultsFD[0]['data'][variable], 'anomaly': resultsFD[0]['data']['anomaly_scores']})

        # Filtrar las anomalias
        anomaly_result = originalDf[originalDf['anomaly'] <= filter] 
        # Filtrar las no anomalias
        no_anomaly_result = originalDf[originalDf['anomaly'] > filter] 

        # Contar el total de anomalias por atributo
        anomalyTable = anomaly_result.groupby(['attribute'],sort=True)['attribute'].count().to_frame('total_anomaly').reset_index()
        
        # Contar el total de no anomalias por atributo
        no_anomalyTable = no_anomaly_result.groupby(['attribute'],sort=True)['attribute'].count().to_frame('total_no_anomaly').reset_index()

        # Crear DF con los labels unicos
        labelsNumpy = originalDf['attribute'].unique()
        labelsDF = pd.DataFrame(labelsNumpy)
        labelsDF.columns= ['attribute']

        # join labels con anomaly
        realData = labelsDF.join(anomalyTable.set_index('attribute'), on='attribute', how='left')

        # join realData con no anomaly
        realData = realData.join(no_anomalyTable.set_index('attribute'), on='attribute', how='left')
        
        # Llenar campos vacios con 0s
        realData = realData.fillna(0)

        # sort realData
        realData.sort_values(by=['total_anomaly'], inplace=True, ascending=False, kind='mergesort')
        realData = realData.reset_index(drop=True)

        data = {
            'type': type,
            'labels': realData['attribute'].tolist(),
            'anomalyList': realData['total_anomaly'].tolist(),
            'noAnomalyList' : realData['total_no_anomaly'].tolist()
            #'normalList': df['normalLists'].tolist()
        }            
    else:
            data = { 'message': 'Not found' }
    return JsonResponse(data)


def searchBarGraph(request, historyID, variable, filter):
    return searchBarLineGraphHelper(request, historyID, variable, filter, "Bar")


def searchLineGraph(request, historyID, variable, filter):
    return searchBarLineGraphHelper(request, historyID, variable, filter, "Line")


def searchBubbleGraph1(request, historyID, attribute1, attribute2, filter):
    filter = float(filter)
    print("start")
    # Usar coleccion "FileData"
    colectionFD = db["FileData"]
    print("coleccion")
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsFD = list(colectionFD.find({"_id": historyID}, {"data." + attribute1 : 1, "data." + attribute2 : 1, "data.anomaly_scores": 1}))
    #print(resultsFD)
    print("resultFD")
    # Si existe el historial
    if len(resultsFD) > 0:
        # Crear data frame
        df =  pd.DataFrame({'attribute1' :resultsFD[0]['data'][attribute1],'attribute2' :resultsFD[0]['data'][attribute2], 
        'anomaly': resultsFD[0]['data']['anomaly_scores']})
        # Filtrar las anomalias
        # ! Igual o menor que??
        rslt_df = df[df['anomaly'] <= filter]
        #print(rslt_df)
        anomalyRelation = df.groupby(['attribute1', 'attribute2']).size().to_frame('size')
        anomalyRelation.reset_index( inplace=True)
        #print(anomalyRelation)
        
        anomalyRelation.sort_values(by=['size'], inplace=True, ascending=False, kind='mergesort')
        bubbleData = []
        #print(anomalyRelation)
        #df.shape[0]
        #df.index
        #print(len(anomalyRelation))
        #print("value1")
        #print(anomalyRelation.iloc[1,0])
        #print("value2")
        #print(anomalyRelation.iloc[0]['size'])

        #print(anomalyRelation)
        attribute1_list = anomalyRelation['attribute1'].values.tolist()
        attribute2_list =  anomalyRelation['attribute2'].values.tolist()

        #df["Courses"].values.tolist()
        #print(attribute2_list)
        for i in range(len(anomalyRelation)):
            bubbleData.append(
                {
                    #'x': str(anomalyRelation.iloc[i]['attribute1']), 
                    #'y': str(anomalyRelation.iloc[i]['attribute2']), 
                    'x': int(i), 
                    'y': int(i), 
                    'r': int(anomalyRelation.iloc[i]['size'])
                }
            )

        #bubbleData = np.array(bubbleData)

        
        data = {
            'type':'Bubble',
            #'labels': anomalyTable['attribute'].tolist(),
            'data' : bubbleData, #.tolist(),
            'attribute1': attribute1_list,
            'attribute2': attribute2_list
            #'normalList': df['normalLists'].tolist()
        }            
    else:
            data = { 'message': 'Not found' }
    return JsonResponse(data)

def searchBubbleGraph2(request, historyID, attribute1, attribute2, filter):
    filter = float(filter)
    print("start")
    # Usar coleccion "FileData"
    colectionFD = db["FileData"]
    print("coleccion")
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsFD = list(colectionFD.find({"_id": historyID}, {"data." + attribute1 : 1, "data." + attribute2 : 1, "data.anomaly_scores": 1}))
    #print(resultsFD)
    print("resultFD")
    # Si existe el historial
    if len(resultsFD) > 0:
        # Crear data frame
        df =  pd.DataFrame({'attribute1' :resultsFD[0]['data'][attribute1],'attribute2' :resultsFD[0]['data'][attribute2], 
        'anomaly': resultsFD[0]['data']['anomaly_scores']})

        # Filtrar las anomalias
         # En caso de que falle el filtrado
        try:
            anomalyFilterDf = df[df['anomaly'] <= filter]
            print("anomalyFilterDf")
            print(anomalyFilterDf)

            # Agrupar anomalias con ambos atributos
            anomalyRelation = anomalyFilterDf.groupby(['attribute1', 'attribute2']).size().to_frame('size')
            anomalyRelation.reset_index(inplace=True)
            print("anomalyRelation")
            print(anomalyRelation)
            # Obtener el valor mas alto de anomaly
                # nlargest retorna un dataframe... iloc retorna el valor
            topAnomalyValue = anomalyRelation.nlargest(1, 'size').iloc[0]['size']
            print("top")

            ratio = 25 / topAnomalyValue

            anomalyRelation['size'] = anomalyRelation['size'].map(lambda x : x * ratio)
            print("anomalymap")

            # ! se borra
            anomalyRelation.sort_values(by=['size'], inplace=True, ascending=False, kind='mergesort')
            print(anomalyRelation)
            
            # lista de valores unicos de attribute1
            attribute1List = anomalyRelation['attribute1'].unique().tolist()
            # lista de valores unicos de attribute2
            attribute2List = anomalyRelation['attribute2'].unique().tolist()

            # Rangos para values en attribute1Dict
            attribute1Range = list(range(0, len(attribute1List), 1))
            # Rangos para values en attribute2Dict
            attribute2Range = list(range(0, len(attribute2List), 1))

            # Juntar attribute1List, attribute1Range para formar diccionario
            # ! Preguntar como esta mejor? Int, Attr? Attr, int?
            attribute1Dict = dict(zip(attribute1List, attribute1Range))
            # Juntar attribute2List, attribute2Range para formar diccionario
            attribute2Dict = dict(zip(attribute2List, attribute2Range))
            print(attribute2Dict)

            # Lista para los datos que graficar
            bubbleDataList = []
            # agrega los datos en bubbledata
            for i in range(len(anomalyRelation)):
                bubbleDataList.append(
                    {
                        'x': int(attribute1Dict[anomalyRelation.iloc[i]['attribute1']]),  # Valor que tiene atributo1 en attribute1Dict
                        'y': int(attribute2Dict[anomalyRelation.iloc[i]['attribute2']]),  # Valor que tiene atributo2 en attribute2Dict
                        'r': int(anomalyRelation.iloc[i]['size'])
                    }
                )

            
            data = {
                'type':'Bubble',
                'data' : bubbleDataList, #.tolist(),
                'attribute1Dict' : attribute1List,
                'attribute2Dict' : attribute2List
            }            
        except:
            data = {'message' : 'No anomalies less than filter: ' + str(filter)}
    else:
            data = { 'message': 'Not found' }

    return JsonResponse(data)



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
        data = {'message': 'Not found'}
    return JsonResponse(data)

def updateGraph(request, historyID, graphID):
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
            newgraph = json.loads(request.body)
            graphs[graphID] = newgraph
            
            # Actualizar el registro con la nueva lista
            collectionRH.update_one({"_id": historyID}, {"$set": {"graphs": graphs}})
            
            data = {'message': 'Success'}
    else:
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
        try: 
            # Sacar las graficas actuales del registro
            graphs = results[0]["graphs"] 
            # Agregar la grafica al registro 
            graphs.append(graph)
        except:
            graphs = [graph]
        
        # Actualizar el registro
        colection.update_one({"_id": historyID}, {"$set": {"graphs": graphs}})
        print("Success")
    else:
        print("updateGraphs: Not found")


# * Pendientes: Documentacion y burbuja
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
    Modelo de datos (Nuevo)

Terminados:
    Modelo de Calidad
    Documento Vision
    Plan de Comunicación
    Plan de Recursos
    Plan y Analisis de Riesgos

'''