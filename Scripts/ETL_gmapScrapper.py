import functions_framework
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
import pandas_gbq
from datetime import datetime
import os
#from google.api_core.exceptions import NotFound  # Importar NotFound para manejar excepciones


def etl_scrapper(request, context=None):
    '''------------ Configura el cliente y carga el archivo json obtenido mediante el scraper -----------'''
    print('--- Configura el cliente y carga el archivo json obtenido mediante el scraper')
    
    # Inicializa el cliente de GCS en el ámbito correcto
    storage_client = storage.Client()
    
    def read_latest_json_from_bucket(bucket_name):
        # Obtén la referencia del bucket
        bucket = storage_client.bucket(bucket_name)
        
        # Lista todos los blobs (archivos) en el bucket
        blobs = list(bucket.list_blobs())
        
        # Filtra solo los archivos JSON
        json_blobs = [blob for blob in blobs if blob.name.endswith('.json')]
        
        # Si no hay archivos JSON, devuelve un mensaje o maneja el caso
        if not json_blobs:
            raise ValueError("No hay archivos JSON en el bucket.")
        
        # Selecciona el archivo más reciente basado en el tiempo de actualización
        latest_blob = max(json_blobs, key=lambda b: b.updated)
        
        # Descarga el contenido del archivo JSON
        json_content = latest_blob.download_as_string()
        
        # Convierte los datos JSON a un DataFrame
        df = pd.read_json(pd.io.common.BytesIO(json_content))
        
        return df

    # Uso de la función
    bucket_name = 'dataset_crawler'
    df = read_latest_json_from_bucket(bucket_name)

    '''------------ Filtra las columnas necesarias -----------'''
    print('---- Filtra las columnas necesarias')
    columns_to_keep = ['title', 'location', 'totalScore', 'categories', 'price', 'reviews']
    df_selected = df[columns_to_keep]

    '''------------ Explota las columnas anidadas o que contienen listas o diccionarios -----------'''
    print('--- Explota las columnas anidadas o que contienen listas o diccionarios')
    df_exploded = df_selected.explode('reviews')
    df_reviews_normalized = pd.json_normalize(df_exploded['reviews'])
    df_location_normalized = pd.json_normalize(df_exploded['location'])

    df_final = df_exploded.reset_index(drop=True).join(df_reviews_normalized).join(df_location_normalized)
    df_final = df_final.explode('categories')

    '''------------ Configura el campo time -----------'''
    print('--- Configura el campo time')
    df_final['publishedAtDate'] = pd.to_datetime(df_final['publishedAtDate'], errors='coerce')
    df_final['time'] = df_final['publishedAtDate'].astype('int64') // 10**6

    '''------------ Crea un nuevo campo con el número de símbolos en el campo price -----------'''
    print('---- Crea un nuevo campo con el número de símbolos en el campo price')
    df_final['price_length'] = df_final['price'].str.len()

    '''------------ Nuevamente filtra las columnas necesarias -----------'''
    print('--- Nuevamente filtra las columnas necesarias')
    columns_to_keep = ['title', 'totalScore', 'categories', 'price', 'text', 'stars', 'lat', 'lng', 'time', 'price_length']
    df_final = df_final[columns_to_keep]

    '''------------ Elimina duplicados -----------'''
    print('-- Elimina duplicados')
    df_final = df_final.drop_duplicates()

    '''------------ Renombra columnas -----------'''
    print('--- Renombra columnas')
    df_final.rename(columns={
        'title': 'name_x', 
        'totalScore': 'avg_rating', 
        'categories': 'category', 
        'stars': 'rating', 
        'lat': 'latitude', 
        'lng': 'longitude'
    }, inplace=True)

    '''----------- Reclasifica los valores de la columna "category" -----------'''
    print('--- Reclasifica los valores de la columna "category"')
    bucket1 = storage_client.bucket('datos-raw-json2')
    blob1 = bucket1.blob('Category_reclass.xlsx')
    reclass_content = blob1.download_as_string()
    reclass_df = pd.read_excel(pd.io.common.BytesIO(reclass_content))

    reclass_df['Original_Category'] = reclass_df['Original_Category'].apply(lambda x: x.strip().lower())
    reclass_df['New_Category'] = reclass_df['New_Category'].apply(lambda x: x.strip())
    reclass_dict = dict(zip(reclass_df['Original_Category'], reclass_df['New_Category']))
    df_final['category'] = df_final['category'].apply(lambda x: x.strip().lower() if isinstance(x, str) else x)
    df_final['category_reclass'] = df_final['category'].map(reclass_dict)

    '''----------- Carga el dataframe a una tabla de BigQuery -----------'''
    print('---- Carga el dataframe a una tabla de BigQuery')

    def create_table_if_not_exists(client, project_id, dataset_id, table_id):
        table_full_id = f'{project_id}.{dataset_id}.{table_id}'
        try:
            client.get_table(table_full_id)
            print(f'Table {table_full_id} already exists.')
        except NotFound:
            schema = [
                bigquery.SchemaField('name_x', 'STRING'),
                bigquery.SchemaField('avg_rating', 'FLOAT'),
                bigquery.SchemaField('category', 'STRING'),
                bigquery.SchemaField('price', 'STRING'),
                bigquery.SchemaField('text', 'STRING'),
                bigquery.SchemaField('rating', 'FLOAT'),
                bigquery.SchemaField('latitude', 'FLOAT'),
                bigquery.SchemaField('longitude', 'FLOAT'),
                bigquery.SchemaField('time', 'INTEGER'),
                bigquery.SchemaField('price_length', 'INTEGER'),
                bigquery.SchemaField('category_reclass', 'STRING')
            ]
            table = bigquery.Table(table_full_id, schema=schema)
            table = client.create_table(table)
            print(f'Table {table_full_id} created successfully.')

    def export_dataframe_to_bigquery(df, project_id, dataset_id, table_id):
        table_full_id = f'{project_id}.{dataset_id}.{table_id}'
        df.to_gbq(destination_table=table_full_id, project_id=project_id, if_exists='replace')
        print(f'DataFrame exported to {table_full_id} successfully.')

    # Configurar el cliente de BigQuery
    client = bigquery.Client()
    project_id = 'pruebasairflow'
    dataset_id = 'GoogleMaps_Dataset'
    table_id = 'scr_google_maps'

    # Crear la tabla si no existe
    create_table_if_not_exists(client, project_id, dataset_id, table_id)

    # Exportar el DataFrame a BigQuery
    export_dataframe_to_bigquery(df_final, project_id, dataset_id, table_id)

    print('Función ETL GoogleMapsScraper ha sido completada exitosamente')

    # Llama la función
# if __name__ == "__main__":
#    print(etl_scraper4(None))