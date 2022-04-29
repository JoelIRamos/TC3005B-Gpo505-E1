from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View

from api.db import db 
from api.functions import *

from bson.json_util import dumps
import json

# from rest_framework.parsers import JSONParser #creo que no se usa
# from django.http import HttpResponse

# Create your views here.

# View del endpoint de searchHistoryList
class searchHistoryListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request):
        return searchHistoryList(request)
    
    def post(self, request):
        return JsonResponse(self.data)
    
    def put(self, request):
        return JsonResponse(self.data)
    
    def delete(self, request):
        return JsonResponse(self.data)

# View del endpoint de searchHistoryDetail
class searchHistoryDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID):
        return searchHistoryDetail(request, historyID)
    
    def post(self, request, historyID=0):
        return JsonResponse(self.data)
    
    def put(self, request, historyID=0):
        return JsonResponse(self.data)
    
    def delete(self, request, historyID=0):
        return JsonResponse(self.data)


# View del endpoint de searchLastSession
class searchLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, userID):
        return searchLastSession(request, userID)
    
    def post(self, request, userID=0):
        return JsonResponse(self.data)
    
    def put(self, request, userID=0):
        return JsonResponse(self.data)
    
    def delete(self, request, userID=0):
        return JsonResponse(self.data)


# View del endpoint de insertLastSession
class insertLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, userID=0, historyID=0):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (POST) del endpoint
    def post(self, request, userID, historyID):
        return insertLastSession(request, userID, historyID)
    
    def put(self, request, userID=0, historyID=0):
        return JsonResponse(self.data)
    
    def delete(self, request, userID=0, historyID=0):
        return JsonResponse(self.data)

# View del endpoint de deleteLastSession
class deleteLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, userID=0): 
        return JsonResponse(self.data)
    
    def post(self, request, userID=0):
        return JsonResponse(self.data)
    
    def put(self, request, userID=0):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (DELETE) del endpoint
    def delete(self, request, userID):
        return deleteLastSession(request, userID)


# View del endpoint de updateLastSession
class updateLastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, userID=0):
        return JsonResponse(self.data)
    
    def post(self, request, userID=0):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (PUT) del endpoint
    def put(self, request, userID):
        return updateLastSession(request, userID)
    
    def delete(self, request, userID=0):
        return JsonResponse(self.data)


# View del endpoint de insertToHistory
class insertToHistoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, userID=0):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (POST) del endpoint
    def post(self, request, userID):
        return insertToHistory(request, userID)
    
    def put(self, request, userID=0):
        return JsonResponse(self.data)
    
    def delete(self, request, userID=0):
        return JsonResponse(self.data)

# class View(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs): 
#         return super().dispatch(request, *args, **kwargs)
    
#     data = {'message': 'endpoint not implemented'}
    
#     def get(self, request):
#         return JsonResponse(self.data)
    
#     def post(self, request):
#         return JsonResponse(self.data)
    
#     def put(self, request):
#         return JsonResponse(self.data)
    
#     def delete(self, request):
#         return JsonResponse(self.data)


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

# class FileView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs): 
#         return super().dispatch(request, *args, **kwargs)
    
#     def get(self, request,id=0):
#         collection = db["File"]
#         if id>0:
#             results = list(collection.find({"_id":id}))
#             # print(results)
#             if len(results)>0:
#                 data = {'message':'found', 'result': results}
#                 # data = {'message':'found', 'result': "a"}
#             else:
#                 data = {'message': 'Not found'}

#         else:
#             results = json.loads(dumps(list(collection.find())))
#             # print(results)
#             if len(results) > 0:
#                 data = {'message': 'Success', 'result': results}
#             else:
#                 data = {'message': 'Empty'}
            
#         return JsonResponse(data)
    
#     def post(self, request):
#         collection = db["File"]
#         jd=json.loads(request.body)
#         # print(jd)
#         collection.insert_many(jd)
#         data = {'message': 'Success'}
#         return JsonResponse(data)
    
#     def put(self, request, id):
#         collection = db["File"]
#         jd = json.loads(request.body)
#         result = list(collection.find({"_id":id}))
#         if len(result)>0:
#             # collection.update_one({"_id":id}, {"$set":{'name':jd['name']}})
#             collection.update_one({"_id":id}, {"$set":jd})
#             datos = {'message': 'Success'}
#         else:
#             datos = {'message': 'Not found'}
#         return JsonResponse(datos)
    
#     def delete(self, request, id):
#         collection = db["File"]
#         result = list(collection.find({"_id":id}))
#         if len(result)>0:
#             collection.delete_one({"_id":id})
#             data = {'message': 'Success'}
#         else:
#             data = {'message': 'Not found'}
#         return JsonResponse(data)