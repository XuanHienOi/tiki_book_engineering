import os

import snowflake.connector
from dotenv import load_dotenv

ENV_PATH = "/home/phinguyen/projects/tiki_book_engineering/airflow/.env"
load_dotenv(ENV_PATH)

account_identifier = os.getenv("SNOWFLAKE_ACCOUNT_IDENTIFIER")
username = os.getenv("SNOWFLAKE_USERNAME")
password = os.getenv("SNOWFLAKE_PASSWORD")
warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
database = os.getenv("SNOWFLAKE_DATABASE")
schema = os.getenv("SNOWFLAKE_SCHEMA")

print(f"Account Identifier: {account_identifier}")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Warehouse: {warehouse}")
print(f"Database: {database}")
print(f"Schema: {schema}")

def connect_to_snowflake(
    account_identifier=account_identifier,
    username=username,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema
):
    conn = snowflake.connector.connect(
            user=username,
            password=password,
            account=account_identifier,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
    return conn

# Function to create table if not exists
def create_table_if_not_exists(conn, table_name, df):
    # Generate CREATE TABLE statement based on the DataFrame columns and data types
    create_table_query = f"CREATE TABLE IF NOT EXISTS {schema}.{table_name} ("
    column_definitions = []

    for column, dtype in df.dtypes.items():
        if dtype == "int64":
            snowflake_type = "INTEGER"
        elif dtype == "float64":
            snowflake_type = "FLOAT"
        elif dtype == "bool":
            snowflake_type = "BOOLEAN"
        elif dtype == "datetime64[ns]":
            snowflake_type = "TIMESTAMP"
        else:
            snowflake_type = "STRING"
        column_definitions.append(f"{column} {snowflake_type}")

    create_table_query += ", ".join(column_definitions) + ")"
    
    # Execute the query
    with conn.cursor() as cur:
        cur.execute(create_table_query)
        print(f"Table '{table_name}' checked/created successfully.")

if __name__ == '__main__':
    conn = connect_to_snowflake()
    if conn:
        with conn:
            print("Connect to snowflake successfully!")


