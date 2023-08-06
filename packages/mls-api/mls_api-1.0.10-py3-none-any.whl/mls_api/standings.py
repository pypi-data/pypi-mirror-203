import os, json
import requests

BASE_URL = "https://mlssoccerapi.com/standings"

bearerToken = os.getenv('BEARER_TOKEN')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {bearerToken}'
}

def get_all_standings():
    response = requests.get(BASE_URL, headers=headers)
    return response.text

def get_standing_by_id(standing_id):
    url = f"{BASE_URL}/{standing_id}"
    response = requests.get(url, headers=headers)
    return response.text

def update_standing_by_id(standing_id, data):
    url = f"{BASE_URL}/{standing_id}"
    payload = json.dumps(data)
    response = requests.put(url, headers=headers, data=payload)
    return response.text

def delete_standing_by_id(standing_id):
    url = f"{BASE_URL}/{standing_id}"
    response = requests.delete(url, headers=headers)
    return response.text

def add_new_standing(data):
    payload = json.dumps(data)
    response = requests.post(BASE_URL, headers=headers, data=payload)
    return response.text
