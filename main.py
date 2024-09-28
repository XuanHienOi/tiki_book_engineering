from db.database import create_tables
from services.category_processor import process_all_categories


def main():
    create_tables()
    process_all_categories()


if __name__ == "__main__":
    main()
