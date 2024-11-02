from datetime import datetime, timedelta

import pandas as pd

from .etl.extract import query_data_from_sqliteDB
from .etl.transform import transform
from .etl.load import load_data_into_snowflake

def incrementally_ETL():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    today_str = today.strftime('%Y-%m-%d')
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    query = f"""
        SELECT * 
        FROM books 
        WHERE DATE(crawl_time) = '{today_str}' 
        OR DATE(crawl_time) = '{yesterday_str}';
        """

    data = query_data_from_sqliteDB(query=query)
    # print(data.dtypes)
    transformed_data = transform(data)
    transformed_data['crawl_time'] = pd.to_datetime(transformed_data['crawl_time'], errors='coerce')
    # print(transformed_data.dtypes)
    df_filtered = transformed_data[transformed_data['crawl_time'].dt.date != yesterday]
    load_data_into_snowflake(table_name="BOOKS", df=df_filtered)
