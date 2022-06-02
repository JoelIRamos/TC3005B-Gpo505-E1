from email.mime import base
import queue
import django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
from django.core.files.storage import default_storage
from django.http import HttpResponse

from api.db import db 
from api.functions import *

# from bson.json_util import dumps

# import pandas as pd
import numpy as np
from datetime import datetime
from os.path import exists

from .forms import UploadFileForm
from .tasks import process_file

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
    
    def post(self, request, historyID='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0'):
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0'):
        return JsonResponse(self.data)


# View del endpoint de searchLastSession
class searchHistoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID):
        return searchHistory(request, historyID)
    
    def post(self, request, historyID='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0'):
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0'):
        return JsonResponse(self.data)

# View del endpoint de searchBarGraph
class searchBarGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID, attribute, filter):
        return searchBarGraph(request, historyID, attribute, filter)
    
    def post(self, request, historyID='0', attribute='0', filter='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0', attribute='0', filter='0'): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0', attribute='0', filter='0'):
        return JsonResponse(self.data)

# View del endpoint de searchLineGraph
class searchLineGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID, attribute, filter):
        return searchLineGraph(request, historyID, attribute, filter)
    
    def post(self, request, historyID='0', attribute='0', filter='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0', attribute='0', filter='0'): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0', attribute='0', filter='0'):
        return JsonResponse(self.data)


# View del endpoint de searchBubbleGraph
class searchBubbleGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID, attribute1, attribute2, filter):
        return searchBubbleGraph2(request, historyID, attribute1, attribute2, filter)
    
    def post(self, request, historyID='0', attribute='0', attribute2='0', filter='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0', attribute='0', attribute2='0', filter='0'): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0', attribute='0', attribute2='0', filter='0'):
        return JsonResponse(self.data)


# View del endpoint de searchHistoryStatistics
class searchStatisticsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID, filter):
        return searchStatistics(request, historyID, filter)
    
    def post(self, request, historyID='0', filter='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0', filter='0'): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0', filter='0'):
        return JsonResponse(self.data)

# View del endpoint de getStatus
class searchStatusView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, historyID):
        return searchStatus(request, historyID)

    def post(self, request, historyID='0'):
        return JsonResponse(self.data)
    
    def put(self, request, historyID='0'): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID='0'):
        return JsonResponse(self.data)


# View del endpoint de updateGraph
class updateGraphsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, historyID='0'): 
        return JsonResponse(self.data)
    
    def post(self, request, historyID='0'):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (PUT) del endpoint
    def put(self, request, historyID):
        return updateGraphs(request, historyID)
    
    def delete(self, request='0', historyID='0'):
        return JsonResponse(self.data)


class FileUploadView(View):
    """File upload view that manages file uploads and proccesing
    """

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def save_file_to_storage(self, file):
        """Saves the file to the storage

        Args:
            file (file): file to be processed

        Returns:
            tuple: (file name, file id, base name, date)
        """        
        # Get current time
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Get the file name without extension
        base_file_name = file.name.replace(' ', '_').replace('.csv','')
        
        # Create the file id
        run_id = base_file_name + '_' + date
        
        # Saves the file in the default storage
        file_name = default_storage.save(run_id+'.csv', file)
        
        return file_name, run_id, base_file_name, date

    def add_to_queue(self, file_id: str) -> np.array:
        """Adds the file to the queue

        Args:
            file_id (str): id of the file to be added to the queue
            
        Returns:
            queue: queue with the file id
        """        
        # creates a new queue if it doesn't exist
        queue = np.array([])
        if not exists('../API_PROJECT/queue.npy'):
            queue = np.append(queue, file_id)
        else:
            queue = np.load('queue.npy')
            queue = np.append(queue, file_id)
        
        # Saves the queue
        saved = False
        while (not saved):
            try:
                np.save('queue.npy', queue)
                saved = True
            except:
                print('Error saving queue, trying again...')
                
        return queue
    
    def post(self, request) -> JsonResponse:
        """Post method for the file upload

        Args:
            request (WSGIRequest): request object

        Returns:
            JsonResponse: The response object
        """
        try:
            # Get the file from the request
            file = request.FILES['file']
            
            # internal_attributes = ['ID_TRANSPORTISTA','weightDifference','D_UBICACION','USUARIO_EGRESO','N_PESO_TARA','mediana']
            # external_attributes = ['C_ID_ORDEN_CABECERA','C_POSICION_ORDEN','Q_CANTIDAD','N_PESO_BRUTO','TIPO_TRANSPORTE']
            # informational_attributes = ['C_SOCIEDAD','D_PATENTE']
            # Gets internal and external attributes from request
            internal_attributes = json.loads(request.POST['internal_attributes'])
            external_attributes = json.loads(request.POST['external_attributes'])
            informational_attributes = json.loads(request.POST['informational_attributes'])
            
            # print('internal_attributes: ' , internal_attributes, 'type: ', type(internal_attributes))
            # print('external_attributes: ', external_attributes, 'type: ', type(external_attributes))
            # print('informational_attributes: ', informational_attributes, 'type: ', type(informational_attributes))
            
            # Saves the file to the storage and gets the file name, file id, base name and date
            file_name, run_id, base_file_name, date = self.save_file_to_storage(file)
            print(file_name, run_id, base_file_name, date)
            # Sends the file to the processing function
            process_file.delay(file_name, base_file_name, run_id, date ,internal_attributes, external_attributes, informational_attributes)
            
            # Adds the file to the queue
            queue = self.add_to_queue(run_id)
            
            return JsonResponse({"message": 1, "run_id": run_id, "queue": queue.tolist()})
        except:
            return JsonResponse({"message": 0})
        
    
    
    def get(self, request) -> UploadFileForm:
        """Get method for the file upload

        Args:
            request (request): The request object

        Returns:
            render: Renders the file upload page
        """
        queue = np.load('queue.npy')
        return render(request, 'upload_file.html', {'form': UploadFileForm()})
        return JsonResponse({"queue": queue.tolist()})


    

