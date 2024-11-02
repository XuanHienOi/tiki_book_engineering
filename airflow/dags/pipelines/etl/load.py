import os

from snowflake.connector.pandas_tools import write_pandas
import pandas as pd

from ..warehouse.snowflake_connection import connect_to_snowflake, create_table_if_not_exists

def load_data_into_snowflake(table_name, df: pd.DataFrame):
    # Ensure column names are uppercase
    df.columns = [col.upper() for col in df.columns]
    
    # Reset index to avoid warnings and compatibility issues
    df = df.reset_index(drop=True)
    conn = connect_to_snowflake()
    with conn:
        table_name = "BOOKS"  # Replace with your target table name
        create_table_if_not_exists(conn, table_name, df)
        
        # Now insert the data from the DataFrame
        success, num_chunks, num_rows, output = write_pandas(
            conn=conn,
            df=df,
            table_name=table_name,
        )
        if success:
            print(f"DataFrame loaded successfully with {num_rows} rows.")
        else:
            print("Failed to load DataFrame.")