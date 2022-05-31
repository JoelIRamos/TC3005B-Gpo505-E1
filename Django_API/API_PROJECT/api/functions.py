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
        # file = fileResults[0]["data"]
        # Buscar el registro de la coleccion "History" que tiene el historyID correspondiente
        ExtIntResults = db["RunHistory"].find_one({"_id": historyID})
        
        # Extraer las graficas      
        try:
            graphs = ExtIntResults["graphs"]
        except:
            graphs = []
        
        # Formato de los Datos
        data = {
            'message':'found',
            'result': {
                'historyID': historyID,
                'base_file_name': ExtIntResults["base_file_name"],
                'date': ExtIntResults["date"],
                'internal_attributes': ExtIntResults["internal_attributes"],
                'external_attributes': ExtIntResults["external_attributes"],
                'informational_attributes': ExtIntResults["informational_attributes"],
                'graphs': graphs,
                # 'data': file
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
        
        # Extraer las graficas
        try:
            graphs = ExtIntResult["graphs"]
        except:
            graphs = []
        # Formato de los Datos
        data = {
            'message':'found',
            'result': {
                'historyID': historyID,
                'base_file_name': ExtIntResult["base_file_name"],
                'date': ExtIntResult["date"],
                'internal_attributes': ExtIntResult["internal_attributes"],
                'external_attributes': ExtIntResult["external_attributes"],
                'informational_attributes': ExtIntResult["informational_attributes"],
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

        # ! Borrar.. No es necesario por el top 25sort realData
        #//realData.sort_values(by=['total_anomaly'], inplace=True, ascending=False, kind='mergesort')
        #//realData = realData.reset_index(drop=True)
        #//print(realData)
        # obtiene las 25 filas con mas anomalias
        realDataTop25 = realData.nlargest(25, 'total_anomaly')

        data = {
            'type': type,
            'labels': realDataTop25['attribute'].tolist(),
            'anomalyList': realDataTop25['total_anomaly'].tolist(),
            'noAnomalyList' : realDataTop25['total_no_anomaly'].tolist()
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
    #//print("start")
    # Usar coleccion "FileData"
    colectionFD = db["FileData"]
    #//print("coleccion")
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsFD = list(colectionFD.find({"_id": historyID}, {"data." + attribute1 : 1, "data." + attribute2 : 1, "data.anomaly_scores": 1}))
    #//print(resultsFD)
    #//print("resultFD")
    # Si existe el historial
    if len(resultsFD) > 0:
        # Crear data frame
        df =  pd.DataFrame({'attribute1' :resultsFD[0]['data'][attribute1],'attribute2' :resultsFD[0]['data'][attribute2], 
        'anomaly': resultsFD[0]['data']['anomaly_scores']})

        # Filtrar las anomalias
        # En caso de que falle el filtrado
        try:
            anomalyFilterDf = df[df['anomaly'] <= filter]
            #//print("anomalyFilterDf")
            #//print(anomalyFilterDf)

            # Agrupar anomalias con ambos atributos
            anomalyRelation = anomalyFilterDf.groupby(['attribute1', 'attribute2']).size().to_frame('size')
            anomalyRelation.reset_index(inplace=True)
            #//print("anomalyRelation")
    
            # Obtener el valor mas alto de anomaly
                # nlargest retorna un dataframe... iloc retorna el valor
            topAnomalyValue = anomalyRelation.nlargest(1, 'size').iloc[0]['size']
            #//print("top")

            ratio = 25 / topAnomalyValue

            anomalyRelation['size'] = anomalyRelation['size'].map(lambda x : x * ratio)

            # ! borrar No es necesario puesto a que final se obtiene los top 25
            # //anomalyRelation.sort_values(by=['size'], inplace=True, ascending=False, kind='mergesort')
            # //print(anomalyRelation)

            anomalyRelationTop25 = anomalyRelation.nlargest(25, 'size')
            
            # lista de valores unicos de attribute1
            attribute1List = anomalyRelationTop25['attribute1'].unique().tolist()
            # lista de valores unicos de attribute2
            attribute2List = anomalyRelationTop25['attribute2'].unique().tolist()

            # Rangos para values en attribute1Dict
            attribute1Range = list(range(0, len(attribute1List), 1))
            # Rangos para values en attribute2Dict
            attribute2Range = list(range(0, len(attribute2List), 1))

            # Juntar attribute1List, attribute1Range para formar diccionario
            attribute1Dict = dict(zip(attribute1List, attribute1Range))
            # Juntar attribute2List, attribute2Range para formar diccionario
            attribute2Dict = dict(zip(attribute2List, attribute2Range))
            #//print(attribute2Dict)

            # Lista para los datos que graficar
            bubbleDataList = []
            # agrega los datos en bubbledata
            for i in range(len(anomalyRelationTop25)):
                bubbleDataList.append(
                    {
                        'x': int(attribute1Dict[anomalyRelationTop25.iloc[i]['attribute1']]),  # Valor que tiene atributo1 en attribute1Dict
                        'y': int(attribute2Dict[anomalyRelationTop25.iloc[i]['attribute2']]),  # Valor que tiene atributo2 en attribute2Dict
                        'r': int(anomalyRelationTop25.iloc[i]['size'])
                    }
                )

            # Juntar attribute1Range, attribute1List  para formar diccionario
            attribute1DictBubble = dict(zip(attribute1Range, attribute1List))
            # Juntar attribute2Range, attribute2List  para formar diccionario
            attribute2DictBubble = dict(zip(attribute2Range, attribute2List))

            data = {
                'type':'Bubble',
                'data' : bubbleDataList, #.tolist(),
                'attribute1Dict' : attribute1DictBubble,
                'attribute2Dict' : attribute2DictBubble
            }            
        except:
            data = {'message' : 'No anomalies less than filter: ' + str(filter)}
    else:
            data = { 'message': 'Not found' }

    return JsonResponse(data)


def searchStatistics(request, historyID, filter):
    filter = float(filter)
    
    # Usar coleccion "FileData"
    colectionFD = db["FileData"]
    
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsFD = list(colectionFD.find({"_id": historyID})) # {"data." + attribute1 : 1, "data." + attribute2 : 1, "data.anomaly_scores": 1}
    
    # Si existe el historial
    if len(resultsFD) > 0:

        # ! BRUH
        #// Creacion del data frame
        #// df = pd.DataFrame({labelsList[0] : resultsFD[0]['data'][str(labelsList[0])]})
        #// for i in range(1, len(labelsList)):
        #//     df.insert(i, labelsList[i], resultsFD[0]['data'][str(labelsList[i])])  # assign(TutorsAssigned=resultsFD[0]['data'][labelsList[i]])

        # ? yes
        # Creacion del data frame
        df = pd.DataFrame( resultsFD[0]['data'])

        # Filtrar las anomalias
        # En caso de que falle el filtrado
        try:
            anomalyFilterDf = df[df['anomaly_scores'] <= filter]

            totalLength = len(df)
            anomalyLength = len(anomalyFilterDf)
            anomalyPercentage = float('%.2f'%((anomalyLength / totalLength) * 100))

            # // Filtrado de relaciones anomalas
            # // anomalyFilterDf = dfAnomalyRelation[dfAnomalyRelation['anomaly_scores'] <= filter]
            
            # Nombres de los labels
            labelsList = (list(resultsFD[0]['data'].keys()))
            # No aceptar int float
            for i in labelsList:
                if(anomalyFilterDf[i].dtypes != "object"): # deteccion de int float
                    del anomalyFilterDf[i] # eliminacion de columna
                    # ? Cuidado con la columna total ya que es int64

            # Agrupar anomalias con ambos atributos
            dfGroupAnomalyR = anomalyFilterDf.groupby(list(anomalyFilterDf.columns)).size().to_frame('total')
            dfGroupAnomalyR.reset_index(inplace=True)
            
            # Total de relaciones repetidas
            totalAnomalyRNotUnique =  len(dfGroupAnomalyR[dfGroupAnomalyR["total"] > 1])

            # Total de Relaciones
            totalAnomalyR = len(dfGroupAnomalyR)

            # Porcentaje de relaciones repetidas
            anomalyRelationsPercentage = float('%.2f'%((totalAnomalyRNotUnique / totalAnomalyR) * 100))

            # ? Cantidad de anomalias unicas
            # Datos de las estadisticas
            data = {
                'message': 'Success', 
                'result': {
                    'TotalAnomalys': anomalyLength,
                    'AnomatyPercentage': anomalyPercentage,
                    'AnomalyRelations': totalAnomalyRNotUnique,
                    'AnomalyRelationsPercentage' : anomalyRelationsPercentage
                }
            }
        except:
            data = {'message' : 'No anomalies less than filter: ' + str(filter)}
    else:
            data = { 'message': 'Not found' }
        
    return JsonResponse(data)

def searchStatus(request, historyID):
    print("llenando")
    return JsonResponse({'message': 'Success'})


def updateGraphs(request, historyID):
    # Usar la coleccion "RunHistory"
    collectionRH = db["RunHistory"]
    # Encontrar los registros que tienen el historyID correspondiente (Maximo debe haber 1)
    resultsRH = list(collectionRH.find({"_id": historyID}))
    # Si existe el historial
    if len(resultsRH) > 0:
        # Extraer Graficas del body
        newgraphs = json.loads(request.body)
        
        # Actualizar el registro con la nueva lista
        collectionRH.update_one({"_id": historyID}, {"$set": {"graphs": newgraphs}})
        
        data = {'message': 'Success'}
    else: 
        data = {'message': 'Not found'}
    return JsonResponse(data)


# * Pendientes: Documentacion y burbuja
'''
getStatus
Comment putGraph
Terminar y Actualizar:
    Prioridad:
    Documento de Funcionalidades: Actualizar Backend y agregar Frontend
    Bitacora de Pruebas: Agregar Frontend
    Manual de Usuario (Nuevo)
	Manual de Despliegue (Nuevo)
    Actualizar Modelo de BD
    Y MarkDown

    Later:
    Especificación de Requerimientos Revisar Pequeños Detalles
	Historias de Usuario: Revisar Pequeños Detalles
    Plan de Calidad: Actualizar a las Pruebas Finales


Terminados:
    Modelo de Calidad
    Documento Vision
    Plan de Comunicación
    Plan de Recursos
    Plan y Analisis de Riesgos

'''