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
    
    # def filter_columns(self, df, columns):
    #     """Filters the columns of a dataframe

    #     Args:
    #         df (DataFrame): DataFrame to filter
    #         columns (List): List of columns to keep

    #     Returns:
    #         DataFrame: DataFrame with the columns filtered
    #     """
    #     return df[columns]
    
    # def clean_df(self, df):
    #     """Cleans a dataframe from null or NaN values

    #     Args:
    #         df (DataFrame): Dataframe to clean

    #     Returns:
    #         DataFrame: Cleaned dataframe
    #     """
    #     for column in df:
    #         if df[column].isna().sum() > 0:
    #             df[column] = df[column].fillna('NA')
    
    # # def train_label_encoder(self, df):
    # #     """Trains a label encoder

    # #     Args:
    # #         df (DataFrame): Dataframe to train the label encoder
            
    # #     Returns:
    # #         List: List of Label Encoders
    # #     """
    # #     les = []
    # #     for column in df:
    # #         le = LabelEncoder()
    # #         le.fit(df[column].astype(str))
    # #         les.append(le)
    # #         del le
    # #     return les

    # def encode_labels(self, df):
    #     """Encode labels of a dataframe

    #     Args:
    #         df (DataFrame): DataFrame with the data to categorize
            
    #     Returns:
    #         DataFrame: Dataframe with the encoded labels
    #     """
    #     les = dict()
    #     for column in df:
    #         les[column] = LabelEncoder()
    #         df[str(column)+'_encoded'] = les[column].fit_transform(df[column].astype(str))
    #         df.drop(column, axis=1, inplace=True)
    #     return les

    
    # def decode_labels(self, df, les):
    #     """Decode labels of a dataframe

    #     Args:
    #         df (DataFrame): DataFrame with the data to categorize
            
    #     Returns:
    #         DataFrame: Dataframe with the decoded labels
    #     """
    #     for column in df.iloc[:,:-1]:
    #         name = column.split('_encoded')[0]
    #         les[name].classes_
    #         df[name] = les[name].inverse_transform(df[column])
    #         df.drop(column, axis=1, inplace=True)
    
    # def train_model(self, df, model):
    #     """Trains a model

    #     Args:
    #         df (DataFrame): Dataframe to train the model
    #         model (Model): Model to train
    #     """
    #     model.fit(df)
        
    
    # def apply_model(self, df, model):
    #     """Applies the Isolation Forest algorithm to the dataframe

    #     Args:
    #         df (DataFrame): DataFrame with the data to classify
    #         model (Model): Model to apply
            
    #     Returns:
    #         DataFrame: DataFrame with the data classified
    #     """
    #     df_1 = df.copy()
    #     df['anomaly_scores'] = model.decision_function(df)  

    # def upload_to_db(self, df, collection):
    #     """Uploads the dataframe to a database

    #     Args:
    #         df (DataFrame): Dataframe to upload
    #         collection (Collection): Collection to upload to
    #     """
    #     for index, row in df.iterrows():
    #         collection.insert_one(row.to_dict())
    
    # def process_file(self, file, columns, columns_IF):
    #     """Applies the Isolation Forest algorithm to the file using certain columns

    #     Args:
    #         file (file): File to be processed
    #         columns (list): List of columns in the file
    #         columns_IF (list): List of columns used by the Isolation Forest algorithm

    #     Returns:
    #         : None
    #     """
        
    #     model = IsolationForest(random_state=0, max_features=1, max_samples=91, n_estimators=400, contamination=0.48)
    #     le = LabelEncoder()
    #     chunk_size = 10000
    #     classes = np.array([])
    #     df_p = pd.DataFrame()
        
    #     file.seek(0)
    #     for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False):
    #         chunk.columns = columns
            
    #         df = self.filter_columns(chunk, columns_IF)
    #         self.clean_df(df)
            
    #         # newclasses = self.train_label_encoder(df, le)
    #         # classes = np.unique(np.append(classes, newclasses))
    #         # le.classes_ = classes
            
    #         df_p = pd.concat([df_p, df])
        
    #     #les = self.train_label_encoder(df_p)
    #     les = self.encode_labels(df_p)
    #     #print(les)
    #     self.train_model(df_p, model)
    #     self.apply_model(df_p, model)
    #     self.decode_labels(df_p, les)
    #     #print(df_p)
        
    #     #df_p.to_csv('test.csv')
    #     #self.upload_to_db(df_p, db["File"])
        
    #     # file.seek(0)
    #     # for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False):
    #     #     chunk.columns = columns
    #     #     df = self.filter_columns(chunk, columns_IF)
    #     #     df = self.clean_df(df)
    #     #     df = self.encode_labels(df, le)
    #     #     df = self.apply_model(df, model)
            

    #     #     print(df.isna().sum(), df.shape, df)

        
        
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
            columns = self.get_columns(file)
            file_id = file.name.replace(' ', '_').replace('.csv','') + '_' + datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            
            file_name = default_storage.save(file.name, file)
            
            process_file.delay(file_name, columns, columns_IF)
            
            #self.process_file(file, columns, ['ID_TRANSPORTISTA', 'EMPRESA_TRANSPORTISTA', 'C_ID_ORDEN_CABECERA', 'C_POSICION_ORDEN', 'Q_CANTIDAD'])

            return JsonResponse({"message": "File received", "file_id": file_id})
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


    

