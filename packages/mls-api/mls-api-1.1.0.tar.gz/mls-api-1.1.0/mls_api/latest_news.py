import requests
import json

def get_latest_news(bearer_token, id=None):
    url = 'https://mlssoccerapi.com/news/'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearer_token}'
    }
    if id != None: 
        url += id
    response = requests.get(url=url, headers=headers)
    return response.json()

def update_latest_news(bearer_token, id, payload):
    url = f'https://mlssoccerapi.com/news/{id}'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.put(url=url, headers=headers, json=payload)
    return response.json()

def delete_latest_news(bearer_token, id): 
    url = f'https://mlssoccerapi.com/news/{id}'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.delete(url=url, headers=headers)
    return response.json()

def add_latest_news(bearer_token, payload):
    url = 'https://mlssoccerapi.com/news/'
    headers = {
        'Content-Type': 'application/json', 
        'Authorization': f'Bearer {bearer_token}'
    }
    response = requests.post(url=url, headers=headers, json=payload)
    return response.json()
