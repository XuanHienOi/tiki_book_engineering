import requests
from constants import API_URL, HEADERS, API_DETAILS_URL


def fetch_data_from_api(page, category_id):
    params = {
        'limit': 40,
        'category': category_id,
        'page': page
    }
    try:
        response = requests.get(API_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch data from API: {e}")
        return None


def fetch_data_by_id(id):
    try:
        url = f"{API_DETAILS_URL}{id}"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch data from API: {e}")
        return None
