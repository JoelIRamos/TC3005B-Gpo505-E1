from API_PROJECT.celery import app
from celery import shared_task

from django.core.files.storage import default_storage

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import time
from os.path import exists

# def get_columns(file):
#     """Gets the columns of a file

#     Args:
#         file (file): File to get the columns from

#     Returns:
#         list: List with the columns
#     """    ''''''
#     for chunk in pd.read_csv(file, chunksize=1):
#         return chunk.columns.to_list()

# def filter_columns(df, columns):
#     """Filters the columns of a dataframe

#     Args:
#         df (DataFrame): DataFrame to filter
#         columns (List): List of columns to keep

#     Returns:
#         DataFrame: DataFrame with the columns filtered
#     """
#     return df[columns]
    
def clean_df(df):
    """Cleans a dataframe from null or NaN values

    Args:
        df (DataFrame): Dataframe to clean

    Returns:
        DataFrame: Cleaned dataframe
    """
    for column in df:
        if df[column].isna().sum() > 0:
            df[column] = df[column].fillna('NA')

def encode_labels(df):
    """Encode labels of a dataframe

    Args:
        df (DataFrame): DataFrame with the data to categorize
        
    Returns:
        DataFrame: Dataframe with the encoded labels
    """
    les = dict()
    for column in df:
        les[column] = LabelEncoder()
        df[str(column)+'_encoded'] = les[column].fit_transform(df[column].astype(str))
        df.drop(column, axis=1, inplace=True)
    return les

def decode_labels(df, les):
    """Decode labels of a dataframe

    Args:
        df (DataFrame): DataFrame with the data to categorize
        
    Returns:
        DataFrame: Dataframe with the decoded labels
    """
    for column in df.iloc[:,:-1]:
        name = column.split('_encoded')[0]
        les[name].classes_
        df[name] = les[name].inverse_transform(df[column])
        df.drop(column, axis=1, inplace=True)

def train_model(df, model):
    """Trains a model

    Args:
        df (DataFrame): Dataframe to train the model
        model (Model): Model to train
    """
    model.fit(df)
    
def apply_model(df, model):
    """Applies the Isolation Forest algorithm to the dataframe

    Args:
        df (DataFrame): DataFrame with the data to classify
        model (Model): Model to apply
        
    Returns:
        DataFrame: DataFrame with the data classified
    """
    df['anomaly_scores'] = model.decision_function(df)  

def upload_to_db(df, collection):
    """Uploads the dataframe to a database

    Args:
        df (DataFrame): Dataframe to upload
        collection (Collection): Collection to upload to
    """
    for index, row in df.iterrows():
        collection.insert_one(row.to_dict())

@shared_task
def process_file(file_name, columns_IF):
    """Applies the Isolation Forest algorithm to the file using certain columns

    Args:
        file (file): File to be processed
        columns (list): List of columns in the file
        columns_IF (list): List of columns used by the Isolation Forest algorithm

    Returns:
        : None
    """
    #file = default_storage.open(file_name)
    #columns = get_columns(file)
    # print(columns)
    model = IsolationForest(random_state=0, max_features=1, max_samples=91, n_estimators=400, contamination=0.48)
    chunk_size = 10000
    df_p = pd.DataFrame()

    #file.seek(0)
    file = default_storage.open(file_name)
    for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False, usecols=columns_IF):
        #chunk.columns = columns
        #df = filter_columns(chunk, columns_IF)
        df = chunk
        clean_df(df)
        df_p = pd.concat([df_p, df])

    les = encode_labels(df_p)

    train_model(df_p, model)
    apply_model(df_p, model)

    decode_labels(df_p, les)

    print(df_p)
    df_p.to_csv(file_name.replace('.csv', '_processed.csv'), index=False)

    file.close()
    del file

    default_storage.delete(file_name)
    queue = np.array([])
    if not exists('queue.npy'):
        queue = np.delete(queue, 0)
    else:
        queue = np.load('queue.npy')
        queue = np.delete(queue, 0)
    
    saved = False
    while (not saved):
        try:
            np.save('queue.npy', queue)
            saved = True
        except:
            print('Error saving queue, trying again...')
    
    time.sleep(2)
    
    #df_p.to_csv('test.csv')
    #upload_to_db(df_p, db["File"])