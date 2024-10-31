<<<<<<< Updated upstream
from .db.database import create_tables
from .services.category_processor import process_all_categories
=======
from db.database import create_books_table, create_tables
from services.category_processor import process_all_book_with_id, process_all_categories
import os
>>>>>>> Stashed changes


def main():
    create_tables()
    process_all_categories()

    current_directory = os.getcwd()
    print(f"Current Working Directory: {current_directory}")


if __name__ == "__main__":
    main()
