from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import JsonResponse
from django.views import View

from api.db import db 
from api.functions import *

from bson.json_util import dumps
from .forms import UploadFileForm
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

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


# View del endpoint de updateHistory
class updateHistoryView(View):
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
        return updateHistory(request, userID)
    
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


class FileUploadView(View):
    """File upload view that manages file uploads and proccesing
    """
    filesProcessing = []

    @method_decorator(csrf_exempt)    
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def get_columns(self, file):
        """Returns de columns of a csv file as a list

        Args:
            file (file): csv file

        Returns:
            list: List of strings with the columns of the csv file
        """
        for chunk in pd.read_csv(file, chunksize=1):
            #print(chunk.columns.to_list()) 
            return chunk.columns.to_list()
    
    def clean_df(self, df):
        """Cleans a dataframe from null or NaN values

        Args:
            df (DataFrame): Dataframe to clean

        Returns:
            DataFrame: Cleaned dataframe
        """
        
        return df
    
    def train_label_encoder(self, df, le):
        """Trains a label encoder

        Args:
            df (DataFrame): Dataframe to train the label encoder

        Returns:
            LabelEncoder: Trained label encoder
        """
        return le.fit(df)
    
    def encode_labels(self, df):
        """Encode labels of a dataframe

        Args:
            df (DataFrame): DataFrame with the data to categorize
            
        Returns:
            DataFrame: Dataframe with the encoded labels
        """
        
        return df
    
    def train_model(self, df, model):
        """Trains a model

        Args:
            df (DataFrame): Dataframe to train the model
            model (Model): Model to train

        Returns:
            Model: Trained model
        """
        return model.fit(df)
    
    def apply_model(self, df):
        """Applies the Isolation Forest algorithm to the dataframe

        Args:
            df (DataFrame): DataFrame with the data to classify

        Returns:
            DataFrame: DataFrame with the data classified
        """
        #model = IsolationForest(random_state=0, max_features=1, max_samples=91, n_estimators=400, contamination=0.48)
        #model1 = IsolationForest(random_state=0, max_features=1, max_samples=91, n_estimators=400, contamination=0.48)
        #df_3 = model1.fit(df_2)
        #df_1['scores'] = model.decision_function(x)
        #df_1['anomaly_score'] = model.predict(x)
        #df_3['scores'] = model1.decision_function(x)
        #df_3['anomaly_score'] = model1.predict(x)
        
        #df_1[df_1['anomaly_score']==1].head()
        #df_3[df_3['anomaly_score']==1].head()
        
        return df
        
    def process_file(self, file, columns, columns_IF):
        """Applies the Isolation Forest algorithm to the file using certain columns

        Args:
            file (file): File to be processed
            columns (list): List of columns in the file to be used for the classification
            columns_IF (list): List of columns used by the Isolation Forest algorithm

        Returns:
            : None
        """
        
        model = IsolationForest(random_state=0, max_features=1, max_samples=91, n_estimators=400, contamination=0.48)
        le = LabelEncoder()
        chunk_size = 10000
        
        file.seek(0)
        for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False):
            chunk.columns = columns
            x = chunk[columns_IF]

            print(x.isna().sum(), x.shape, x)
            
        file.seek(0)
        for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False):
            chunk.columns = columns
            x = chunk[columns_IF]
            df = df.append(x)
            print(x.isna().sum(), x.shape, x)

        
        
    def post(self, request):
        """Post method for the file upload

        Args:
            request (request): The request object

        Returns:
            HttpResponse: Contains a list of the columns of the csv file
        """
        file = request.FILES['file']
        if file != None:
            columns = self.get_columns(file)
            self.process_file(file, columns, ['ID_TRANSPORTISTA', 'EMPRESA_TRANSPORTISTA'])
            return JsonResponse(columns, safe=False)
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


    

