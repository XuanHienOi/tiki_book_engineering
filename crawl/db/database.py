import sqlite3


def connect_to_db(db_name='tiki_data.db'):
    return sqlite3.connect(db_name)


def create_tables():
    with connect_to_db() as conn:
        with open('/opt/airflow/dags/crawl/sql/create_tables.sql', 'r') as f:
            conn.executescript(f.read())
