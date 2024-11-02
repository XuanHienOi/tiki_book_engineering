from etl.extract import query_data_from_sqliteDB
from etl.transform import transform
from etl.load import load_data_into_snowflake

if __name__ == "__main__":
    query = "SELECT * FROM books"
    crawl_books_df = query_data_from_sqliteDB(query)
    transformed_df = transform(crawl_books_df)
    load_data_into_snowflake(table_name="BOOKS", df=transformed_df)