from API_PROJECT.celery import app
from celery import shared_task

from django.core.files.storage import default_storage

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

queued_files = []

def get_queued_files():
    """Gets the queued files

    Returns:
        List: List with the queued files
    """
    return queued_files

def filter_columns(df, columns):
        """Filters the columns of a dataframe

        Args:
            df (DataFrame): DataFrame to filter
            columns (List): List of columns to keep

        Returns:
            DataFrame: DataFrame with the columns filtered
        """
        return df[columns]
    
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
    df_1 = df.copy()
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
def process_file(file_name, columns, columns_IF):
    """Applies the Isolation Forest algorithm to the file using certain columns

    Args:
        file (file): File to be processed
        columns (list): List of columns in the file
        columns_IF (list): List of columns used by the Isolation Forest algorithm

    Returns:
        : None
    """
    file = default_storage.open(file_name)
    queued_files.append(file_name)
    
    model = IsolationForest(random_state=0, max_features=1, max_samples=91, n_estimators=400, contamination=0.48)
    le = LabelEncoder()
    chunk_size = 10000
    classes = np.array([])
    df_p = pd.DataFrame()
    
    file.seek(0)
    for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False):
        chunk.columns = columns
        
        df = filter_columns(chunk, columns_IF)
        clean_df(df)
        
        # newclasses = train_label_encoder(df, le)
        # classes = np.unique(np.append(classes, newclasses))
        # le.classes_ = classes
        
        df_p = pd.concat([df_p, df])
    
    #les = train_label_encoder(df_p)
    les = encode_labels(df_p)
    #print(les)
    train_model(df_p, model)
    apply_model(df_p, model)
    decode_labels(df_p, les)
    print(df_p)
    df_p.to_csv(file_name.replace('.csv', '_processed.csv'), index=False)
    #default_storage.save('test.csv',df_p.to_csv('test.csv'))

    
    del file
    
    default_storage.delete(file_name)
    
    #df_p.to_csv('test.csv')
    #upload_to_db(df_p, db["File"])
    
    # file.seek(0)
    # for chunk in pd.read_csv(file, chunksize=chunk_size, low_memory=False):
    #     chunk.columns = columns
    #     df = filter_columns(chunk, columns_IF)
    #     df = clean_df(df)
    #     df = encode_labels(df, le)
    #     df = apply_model(df, model)
        

    #     print(df.isna().sum(), df.shape, df)