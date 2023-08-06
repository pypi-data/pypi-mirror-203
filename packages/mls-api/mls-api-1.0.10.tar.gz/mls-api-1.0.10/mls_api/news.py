import json
import requests

BASE_URL = "https://mlssoccerapi.com/news"

headers = {
    'Content-Type': 'application/json'
}

def get_all_news(auth_header):
    response = requests.get(BASE_URL, headers={**headers, **auth_header})
    return response.text

def get_news_by_id(news_id, auth_header):
    url = f"{BASE_URL}/{news_id}"
    response = requests.get(url, headers={**headers, **auth_header})
    return response.text

def update_news_by_id(news_id, data, auth_header):
    url = f"{BASE_URL}/{news_id}"
    payload = json.dumps(data)
    response = requests.put(url, headers={**headers, **auth_header}, data=payload)
    return response.text

def delete_news_by_id(news_id, auth_header):
    url = f"{BASE_URL}/{news_id}"
    response = requests.delete(url, headers={**headers, **auth_header})
    return response.text

def add_new_news(data, auth_header):
    payload = json.dumps(data)
    response = requests.post(BASE_URL, headers={**headers, **auth_header}, data=payload)
    return response.text
