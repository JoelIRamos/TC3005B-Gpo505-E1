import queue
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View
from django.core.files.storage import default_storage
from django.http import HttpResponse

from api.db import db 
from api.functions import *

from bson.json_util import dumps

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
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


# View del endpoint de searchUserID
class searchUserIDView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, historyID):
        return searchUserID(request, historyID)
    
    # * Metodo HTTP (GET) del endpoint
    def post(self, request, userID=0, historyID=0):
        return JsonResponse(self.data)
    
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


# View del endpoint de updateGraphs
class updateGraphsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, historyID=0):
        return JsonResponse(self.data)
    
    def post(self, request, historyID=0):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (PUT) del endpoint
    def put(self, request, historyID): 
        return updateGraphs(request, historyID)
    
    def delete(self, request, historyID=0):
        return JsonResponse(self.data)

# View del endpoint de searchBarGraph
class searchBarGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, userID):
        return searchBarGraph(request, userID)
    
    def post(self, request, userID=0):
        return JsonResponse(self.data)
    
    def put(self, request, userID=0): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID=0):
        return JsonResponse(self.data)


# View del endpoint de searchBubbleGraph
class searchBubbleGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, userID):
        return searchBubbleGraph(request, userID)
    
    def post(self, request, userID=0):
        return JsonResponse(self.data)
    
    def put(self, request, userID=0): 
        return JsonResponse(self.data)
    
    def delete(self, request, historyID=0):
        return JsonResponse(self.data)


# View del endpoint de searchAreaGraph
class searchLineGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    # * Metodo HTTP (GET) del endpoint
    def get(self, request, userID):
        return searchLineGraph(request, userID)
    
    def post(self, request, userID=0):
        return JsonResponse(self.data)
    
    def put(self, request, userID=0): 
        return JsonResponse(self.data)
    
    def delete(self, request, userID=0):
        return JsonResponse(self.data)


# View del endpoint de deleteGraph
class deleteGraphView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    data = {'message': 'endpoint not implemented'}
    
    def get(self, request, userID=0, graphID=0): 
        return JsonResponse(self.data)
    
    def post(self, request, userID=0, graphID=0):
        return JsonResponse(self.data)
    
    def put(self, request, userID=0, graphID=0):
        return JsonResponse(self.data)
    
    # * Metodo HTTP (DELETE) del endpoint
    def delete(self, request, userID, graphID):
        return deleteGraph(request, userID, graphID)


class FileUploadView(View):
    """File upload view that manages file uploads and proccesing
    """

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        """Post method for the file upload

        Args:
            request (request): The request object

        Returns:
            HttpResponse: Contains a list of the columns of the csv file
        """
        #columns_IF = request.data['columns_IF']
        columns_IF = ['ID_TRANSPORTISTA', 'EMPRESA_TRANSPORTISTA', 'C_ID_ORDEN_CABECERA', 'C_POSICION_ORDEN', 'Q_CANTIDAD']
        file = request.FILES['file']
        if file != None:
            file_id = file.name.replace(' ', '_').replace('.csv','') + '_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            file_name = default_storage.save(file_id+'.csv', file)
            
            process_file.delay(file_name, columns_IF)

            queue = np.array([])
            
            if not exists('../API_PROJECT/queue.npy'):
                queue = np.append(queue, file_id)
            else:
                queue = np.load('queue.npy')
                queue = np.append(queue, file_id)
            
            saved = False
            while (not saved):
                try:
                    np.save('queue.npy', queue)
                    saved = True
                except:
                    print('Error saving queue, trying again...')
            
            return JsonResponse({"message": "File received", "file_id": file_id, "queue": queue.tolist()})
        else:
            return JsonResponse({"message": "No file"})
        #return HttpResponse("Name of file is: " + str(file))
        
    
    
    def get(self, request):
        """Get method for the file upload

        Args:
            request (request): The request object

        Returns:
            render: Renders the file upload page
        """
        return render(request, 'upload_file.html', {'form': UploadFileForm()})





        """
        chunk = 1024*1024   # Process 1 MB at a time.
        f = np.memmap("test.csv")
        num_newlines = sum(np.sum(f[i:i+chunk] == ord('\n'))
                        for i in range(0, len(f), chunk))
        del f
        """


    

