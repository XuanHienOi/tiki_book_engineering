import sqlite3
import pandas as pd

def connect_to_db(db_path='/home/phinguyen/projects/tiki_book_engineering/airflow/tiki_data.db'):
    return sqlite3.connect(db_path)

def query_data_from_sqliteDB(query):
    with connect_to_db() as conn:
        try:
            # cursor.execute(query)
            # results = cursor.fetchall()
            # return results
            df = pd.read_sql_query(query, conn)
            print("Successfully fetch data from sqliteDB!")
            return df
        except sqlite3.Error as e:
            print(f"An error occured: {e}")
            return None

if __name__ == "__main__":
    query = """SELECT * FROM books"""
    books_df = query_data_from_sqliteDB(query)
    print(books_df.head())
    print(books_df.dtypes)
