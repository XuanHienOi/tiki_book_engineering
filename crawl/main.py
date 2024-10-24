from db.database import create_books_table, create_tables
from services.category_processor import process_all_book_with_id, process_all_categories


def main():
    # create_tables()
    # process_all_categories()
    create_books_table()
    process_all_book_with_id()


if __name__ == "__main__":
    main()
