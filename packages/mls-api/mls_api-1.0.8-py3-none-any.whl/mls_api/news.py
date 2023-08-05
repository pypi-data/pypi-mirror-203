import os, json
import requests

BASE_URL = "https://mlssoccerapi.com/news"

bearerToken = os.getenv('BEARER_TOKEN')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {bearerToken}'
}

def get_all_news():
    response = requests.get(BASE_URL, headers=headers)
    return response.text

def get_news_by_id(news_id):
    url = f"{BASE_URL}/{news_id}"
    response = requests.get(url, headers=headers)
    return response.text

def update_news_by_id(news_id, data):
    url = f"{BASE_URL}/{news_id}"
    payload = json.dumps(data)
    response = requests.put(url, headers=headers, data=payload)
    return response.text

def delete_news_by_id(news_id):
    url = f"{BASE_URL}/{news_id}"
    response = requests.delete(url, headers=headers)
    return response.text

def add_new_news(data):
    payload = json.dumps(data)
    response = requests.post(BASE_URL, headers=headers, data=payload)
    return response.text
