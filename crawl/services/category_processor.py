import json

from ..constant import CATEGORIES
from ..db.insert_data import insert_product
from ..services.fetch_data import fetch_data_from_api


def fetch_total_pages(initial_data):
    paging_info = initial_data.get('paging', {})
    return paging_info.get('last_page', 1)


def process_page_data(page_data):
    products = page_data.get('data', [])
    for product in products:
        insert_product(product)


def process_all_pages(total_pages, category_id, category_name):
    for page in range(2, total_pages + 1):
        print(f"Processing page {page} for category {category_name}...")
        page_data = fetch_data_from_api(page, category_id)
        if page_data:
            process_page_data(page_data)


def process_category(category):
    category_id = category['id']
    category_name = category['name']
    print(f"Processing category: {category_name} (ID: {category_id})")

    initial_data = fetch_data_from_api(1, category_id)
    if not initial_data:
        print("No data retrieved from the API.")
        return

    process_page_data(initial_data)
    total_pages = fetch_total_pages(initial_data)
    process_all_pages(total_pages, category_id, category_name)


def process_all_categories():
    for category in CATEGORIES:
        process_category(category)
