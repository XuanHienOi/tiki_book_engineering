import sqlite3
import pandas as pd


def connect_to_db(db_name='tiki_data.db'):
    return sqlite3.connect(db_name)

conn = connect_to_db()
query = "SELECT * FROM products LIMIT 1"
df = pd.read_sql_query(query, conn)
print(df)
conn.close()