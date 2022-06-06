import code
import json
from operator import attrgetter
from API_PROJECT.celery import app
from celery import shared_task
from api.db import db 
from .classes import RunIdInfo, Attributes

from django.core.files.storage import default_storage

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import time
from os.path import exists

    
def clean_df(df: pd.DataFrame):
    """Cleans a dataframe from null or NaN values

    Args:
        df (DataFrame): Dataframe to clean
    """
    # Iterates over the columns of the dataframe and cleans the data
    for column in df:
        # Fils the null values with the a 'NA' string if at least one value is null
        if df[column].isna().sum() > 0:
            df[column] = df[column].fillna('NA')

def load_file_to_df(file_name: str, attributes: Attributes) -> pd.DataFrame:
    """loads a csv file to a dataframe

    Args:
        file_name (str): Name of the file to load
        columns_to_keep (list): List of columns to keep
    Returns:
        DataFrame: Dataframe with the data
    """    
    # Creates a dataframe to store the data from the file
    df_whole = pd.DataFrame()
    # Opens the file

    # with open(file_name, 'rb') as f:
    #     enc = chardet.detect(f.read())['encoding']
    # print(enc)

    file = default_storage.open(file_name)
    #encoding='ISO-8859-1'
    # Reads the file in chunks of 10000 lines at a time and stores the data in the dataframe
    for chunk in pd.read_csv(file, chunksize=10000, low_memory=False, usecols=attributes.all_attributes, delimiter=','):
        # Cleans the dataframe from null or NaN values
        clean_df(chunk)
        # Appends the cleaned chunk to the dataframe to store the data
        df_whole = pd.concat([df_whole, chunk])

    df_model = df_whole.loc[:, attributes.model_attributes]
    # Closes the file
    file.close()
    # Deletes the file variable
    del file
    # Delete the file from the storage
    default_storage.delete(file_name)
    
    # Returns the dataframe with the data
    return df_whole, df_model

def encode_labels(df: pd.DataFrame) -> dict:
    """Encode labels of a dataframe

    Args:
        df (DataFrame): DataFrame with the data to categorize
        
    returns:
        dict: Dictionary with the label encoders
    """
    # Creates a dictionary to store the label encoders
    les = dict()
    # Iterates over the columns of the dataframe and encodes the labels
    for column in df:
        # Creates a label encoder for the column and stores it in the dictionary
        les[column] = LabelEncoder()
        # Encodes the labels and stores them in a new column in the dataframe
        df[str(column)+'_encoded'] = les[column].fit_transform(df[column].astype(str))
        # Drops the original column
        df.drop(column, axis=1, inplace=True)
    return les

def decode_labels(df: pd.DataFrame, les: dict):
    """Decode labels of a dataframe

    Args:
        df (DataFrame): DataFrame with the data to categorize
        les (dict): Dictionary with the label encoders
    """
    # Iterates over the columns of the dataframe and decodes the labels
    for column in df.iloc[:,:-1]:
        # Gets name of the column without the encoded suffix
        name = column.split('_encoded')[0]
        # Decodes the labels and stores them in a new column in the dataframe
        df[name] = les[name].inverse_transform(df[column])
        # Drops the encoded column
        df.drop(column, axis=1, inplace=True)

def train_model(df: pd.DataFrame, model: IsolationForest):
    """Trains a model

    Args:
        df (DataFrame): Dataframe to train the model
        model (IsolationForest): Model to train
    """
    # Trains the model
    model.fit(df)
    
def apply_model(df_model: pd.DataFrame, model: IsolationForest, df_whole: pd.DataFrame) -> pd.DataFrame:
    """Applies a trained Isolation Forest algorithm to the dataframe

    Args:
        df (DataFrame): DataFrame with the data to classify
        model (IsolationForest): Model to apply
        
    Returns:
        DataFrame: DataFrame with the data classified
    """
    # Applies the model to the dataframe and adds the result to the dataframe
    df_whole['anomaly_scores'] = model.decision_function(df_model)  

def update_data_entry(file_data_collection, ref, new_column_name, new_column):
    #file_data_collection.find_one_and_update({'_id': ref}, {'$push': {'data': { new_column_name : new_column}}})
    file_data_collection.find_one_and_update({'_id': ref}, {'$set': {'data.' + new_column_name: new_column}})
    #coll.update({'ref': ref}, {'$push': {'data': new_column}})

def upload_to_db_error(run_id_info: RunIdInfo, attributes: Attributes, error_code: str ,error_message: str):
    history_collection = db['RunHistory']
    history_collection.insert_one({
        "_id" : run_id_info.run_id,
        "base_file_name" : run_id_info.base_file_name,
        "date" : run_id_info.date,
        "internal_attributes" : attributes.internal_attributes,
        "external_attributes" : attributes.external_attributes,
        "informational_attributes" : attributes.informational_attributes,
        "status" : {
            "code": error_code,
            "message": error_message
        }
    })
    
    remove_from_queue(run_id_info.run_id)

def upload_to_db_success(df: pd.DataFrame, run_id_info: RunIdInfo, attributes: Attributes):
    """Uploads the data to the database if the run was successful

    Args:
        df (DataFrame): Dataframe to upload
        file_name (str): Name of the file to upload
        base_file_name (str): Name of the file without extension and date
        date (str): Date of the file
        internal_attributes (list): List of internal attributes
        external_attributes (list): List of external attributes
        informational_attributes (list): List of informational attributes
    """
    # Gets collections references from database
    history_collection = db['RunHistory']
    file_data_collection = db['FileData']
    
    
    # Creates a new document in the file data collection with the data of the processed file
    file_data_collection.insert_one({
        "_id" : run_id_info.run_id
        # "data" : df.to_dict(orient='list')
    })

    # Iterates over the columns of the dataframe and uploads them to the database
    for column in df:
        # Uploads the column to the database
        update_data_entry(file_data_collection, run_id_info.run_id, df[column].name ,df[column].to_list())

    # Creates a new document in the history collection with the data of the run
    history_collection.insert_one({
        "_id" : run_id_info.run_id,
        "base_file_name" : run_id_info.base_file_name,
        "date" : run_id_info.date,
        "internal_attributes" : attributes.internal_attributes,
        "external_attributes" : attributes.external_attributes,
        "informational_attributes" : attributes.informational_attributes,
        "status" : {
            "code": 0,
            "message": ""
        }
    })

def remove_from_queue(file_name: str):
    """Removes a file from the queue

    Args:
        file_name (str): Name of the file to remove
    """
    queue = np.array([])
    if exists('queue.npy'):
        queue = np.load('queue.npy')
        queue = np.delete(queue, np.where(queue == file_name))
    
    # Saves the updated queue
    saved = False
    while (not saved):
        try:
            np.save('queue.npy', queue)
            saved = True
        except:
            print('Error saving queue, trying again...')
    

@shared_task
def process_file(run_id_info_dict: dict, attributes_dict: dict):
    """Reads a csv file, cleans it applies an Isolation Forest algorithm and uploads the data to a database 

    Args:
        file_name (str): Name of the file to process
        base_file_name (str): Name of the file without extension and date
        run_id (str): ID of the file
        date (str): Date of the file
        internal_attributes (list): List of internal attributes to keep
        external_attributes (list): List of external attributes to keep
        informational_attributes (list): List of informational attributes to keep
    """    
    run_id_info = RunIdInfo(**run_id_info_dict)
    attributes = Attributes(**attributes_dict)
    # Combines internal and external attributes to be used in the model

    # Creates model
    model = IsolationForest()
    
    #loads the csv file to a dataframe
    try:
        df_whole, df_model = load_file_to_df(run_id_info.file_name, attributes)
    except:
        upload_to_db_error(run_id_info, attributes, 'E001', 'Hubo un error leyendo el archivo')
        return
    
    # Encodes labels
    try:
        les = encode_labels(df_model)
    except:
        upload_to_db_error(run_id_info, attributes, 'E002', 'Hubo un error codificando las etiquetas')
        return
    
    # Trains the model
    try:
        train_model(df_model, model)
    except:
        upload_to_db_error(run_id_info, attributes, 'E003', 'Hubo un error entrenando el modelo')
        return
        
    # Applies the model to the dataframe 
    try:
        apply_model(df_model, model, df_whole)
    except:
        upload_to_db_error(run_id_info, attributes, 'E004', 'Hubo un error aplicando el modelo')
        return

    # Decodes labels
    #decode_labels(df_model, les)

    # Uploads results to database
    try:
        upload_to_db_success(df_whole, run_id_info, attributes)
    except:
        upload_to_db_error(run_id_info, attributes, 'E005', 'Hubo un error subiendo los datos a la base de datos')
        return
    
    # Removes the file from the queue of files to process
    remove_from_queue(run_id_info.run_id)
            
    #df_whole.to_csv(file_name.replace('.csv','')+'_processed.csv', index=False)