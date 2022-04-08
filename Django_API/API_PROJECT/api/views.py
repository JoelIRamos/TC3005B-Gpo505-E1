from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #creo que no se usa
from rest_framework.parsers import JSONParser #creo que no se usa
from django.http.response import JsonResponse

from api.models import Table
from api.serializers import TableSerializer

from django.utils.decorators import method_decorator
from django.views import View
import json

# Create your views here.

    
class TableView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request,id=0):
        if id>0:
            tables = list(Table.objects.filter(TableID=id).values())
            if len(tables)>0:
                datos = {'message':'found', 'table':tables[0]}
            else:
                datos = {'message': 'Not found'}
            
            return JsonResponse(datos)
        else:
            tables = list(Table.objects.values())
            if len(tables) > 0:
                datos = {'message': 'Success', 'tables': tables}
            else:
                datos = {'message': 'No hay '}
            
            return JsonResponse(datos)
    
    def post(self, request):
        jd=json.loads(request.body)
        # print(jd)
        Table.objects.create(TableID=jd['TableID'], TableName=jd['TableName'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        tables = list(Table.objects.filter(TableID=id).values())
        if len(tables)>0:
            table = Table.objects.get(TableID=id)
            # table.TableID=jd['TableID'] # no se puede cambiar el id, se convierte en un POST
            table.TableName=jd['TableName']
            table.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Not found'}
        return JsonResponse(datos)
    
    def delete(self, request, id):
        tables = list(Table.objects.filter(TableID=id).values())
        if len(tables)>0:
            Table.objects.filter(TableID=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Not found'}
        return JsonResponse(datos)