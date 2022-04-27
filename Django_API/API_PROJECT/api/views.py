from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser #creo que no se usa
from django.http.response import JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
import json

from api.db import db 
from bson.json_util import dumps

# Create your views here.

from django.http import HttpResponse

# View del endpoint de searchHistoryList
class searchHistoryListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request):
        collection = db["History"]
        results = list(collection.find({}))
        if len(results)>0:
            data = {'message':'found', 'result': results}
        else:
            data = {'message': 'Not found'}
        return JsonResponse(data)
    
    def post(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def put(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def delete(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)

# View del endpoint de searchHistoryDetail
class searchHistoryDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID):
        # ToDo: Incluir agentes internos y externos
        collection = db["File"]
        results = list(collection.find({"id_history": historyID}))
        if len(results)>0:
            data = {'message':'found', 'result': results}
        else:
            data = {'message': 'Not found'}
        return JsonResponse(data)
    
    def post(self, request, historyID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def put(self, request, historyID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def delete(self, request, historyID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)


# View del endpoint de searchLastSession
# ToDo: Incluir tabla de File
class searchLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, userID):
        collection = db["LastSession"]
        results = list(collection.find({"_id": userID}))
        if len(results)>0:
            data = {'message':'found', 'result': results}
        else:
            data = {'message': 'Not found'}
        return JsonResponse(data)
    
    def post(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def put(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def delete(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)

# ToDo: Hacer el endpoint de insertLastSession

# View del endpoint de deleteLastSession
class deleteLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def post(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def put(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    # * Metodo HTTP (DELETE) del endpoint
    def delete(self, request, userID):
        collection = db["LastSession"]
        result = list(collection.find({"_id": userID}))
        if len(result)>0:
            collection.delete_one({"_id": userID})
            data = {'message': 'Success'}
        else:
            data = {'message': 'Not found'}
        return JsonResponse(data)
    # ToDo: Delete User


# View del endpoint de updateLastSession
class updateLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def post(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    # * Metodo HTTP (PUT) del endpoint
    def put(self, request, userID):
        # ToDo: Implementar el metodo PUT
        pass
    
    def delete(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)


# View del endpoint de insertToHistory
class insertToHistoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    # * Metodo HTTP (POST) del endpoint
    def post(self, request, userID):
        # ToDo: Implementar el metodo POST
        pass
    
    def put(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def delete(self, request, userID=0):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)

class View(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def post(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def put(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    def delete(self, request):
        data = {'message': 'endpoint not implemented'}
        return JsonResponse(data)
    
    

# from django.http import HttpResponse

# async def searchHistoryList(request):
#     return HttpResponse("<html><h1>searchHistoryList</h1></html>")

# async def searchHistoryDetail(request, historyID):
#     return HttpResponse("searchHistoryDetail: " + str(historyID))

# async def searchLastSession(request, userID):
#     return HttpResponse("searchLastSession: " + str(userID))

# async def deleteLastSession(request, userID):
#     return HttpResponse("deleteLastSession: " + str(userID))

# async def updateLastSession(request, userID):
#     return HttpResponse("updateLastSession: " + str(userID))

# async def insertToHistory(request, userID):
#     if request.method == "POST":
#         return HttpResponse("insertToHistory: " + str(userID))
#     else: 
#         return HttpResponse("NO insertToHistory")

class FileView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        collection = db["File"]
        if id>0:
            results = list(collection.find({"_id":id}))
            # print(results)
            if len(results)>0:
                data = {'message':'found', 'result': results}
                # data = {'message':'found', 'result': "a"}
            else:
                data = {'message': 'Not found'}

        else:
            results = json.loads(dumps(list(collection.find())))
            # print(results)
            if len(results) > 0:
                data = {'message': 'Success', 'result': results}
            else:
                data = {'message': 'Empty'}
            
        return JsonResponse(data)
    
    def post(self, request):
        collection = db["File"]
        jd=json.loads(request.body)
        # print(jd)
        collection.insert_many(jd)
        data = {'message': 'Success'}
        return JsonResponse(data)
    
    def put(self, request, id):
        collection = db["File"]
        jd = json.loads(request.body)
        result = list(collection.find({"_id":id}))
        if len(result)>0:
            # collection.update_one({"_id":id}, {"$set":{'name':jd['name']}})
            collection.update_one({"_id":id}, {"$set":jd})
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Not found'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        collection = db["File"]
        result = list(collection.find({"_id":id}))
        if len(result)>0:
            collection.delete_one({"_id":id})
            data = {'message': 'Success'}
        else:
            data = {'message': 'Not found'}
        return JsonResponse(data)