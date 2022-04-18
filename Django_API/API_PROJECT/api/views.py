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

class HistoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        collection = db["History"]
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
        collection = db["History"]
        jd=json.loads(request.body)
        # print(jd)
        collection.insert_many(jd)
        data = {'message': 'Success'}
        return JsonResponse(data)
    
    def put(self, request, id):
        collection = db["History"]
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
        collection = db["History"]
        result = list(collection.find({"_id":id}))
        if len(result)>0:
            collection.delete_one({"_id":id})
            data = {'message': 'Success'}
        else:
            data = {'message': 'Not found'}
        return JsonResponse(data)


class LastSessionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        datos = {'message': 'Success', 'type': 'GET_LAST_SESSION'}
        return JsonResponse(datos)
    
    def post(self, request):
        datos = {'message': 'Success', 'type': 'POST_LAST_SESSION'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        datos = {'message': 'Success', 'type': 'PUT_LAST_SESSION'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        datos = {'message': 'Success', 'type': 'DELETE_LAST_SESSION'}
        return JsonResponse(datos)

class FileView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        datos = {'message': 'Success', 'type': 'GET_FILE'}
        return JsonResponse(datos)
    
    def post(self, request):
        datos = {'message': 'Success', 'type': 'POST_FILE'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        datos = {'message': 'Success', 'type': 'PUT_FILE'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        datos = {'message': 'Success', 'type': 'DELETE_FILE'}
        return JsonResponse(datos)