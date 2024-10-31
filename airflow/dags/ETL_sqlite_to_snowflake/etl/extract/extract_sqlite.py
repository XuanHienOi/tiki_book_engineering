import sqlite3

def connect_to_db(db_path='/home/phinguyen/projects/tiki_book_engineering/tiki_data.db'):
    return sqlite3.connect(db_path)

def query_data_from_sqliteDB(query):
    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"An error occured: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def extract_table_from_sqliteDB(table_name="books"):
    query = f"SELECT * FROM {table_name}"
    return query_data_from_sqliteDB(query)