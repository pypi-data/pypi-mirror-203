import os, json
import requests

BASE_URL = "https://mlssoccerapi.com/fixtures"

bearerToken = os.getenv('BEARER_TOKEN')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {bearerToken}'
}

def get_all_fixtures():
    response = requests.get(BASE_URL, headers=headers)
    return response.text

def get_fixture_by_id(fixture_id):
    url = f"{BASE_URL}/{fixture_id}"
    response = requests.get(url, headers=headers)
    return response.text

def update_fixture_by_id(fixture_id, data):
    url = f"{BASE_URL}/{fixture_id}"
    payload = json.dumps(data)
    response = requests.put(url, headers=headers, data=payload)
    return response.text

def delete_fixture_by_id(fixture_id):
    url = f"{BASE_URL}/{fixture_id}"
    response = requests.delete(url, headers=headers)
    return response.text

def add_new_fixture(data):
    payload = json.dumps(data)
    response = requests.post(BASE_URL, headers=headers, data=payload)
    return response.text
