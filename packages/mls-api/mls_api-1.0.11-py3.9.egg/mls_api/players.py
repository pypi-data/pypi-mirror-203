import os, json
import requests

def get_all_players(limit=10, offset=0):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/players?limit={limit}&offset={offset}"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def get_player_by_id(player_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/players/{player_id}"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def update_player_by_id(player_id, data):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/players/{player_id}"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text

def delete_player_by_id(player_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/players/{player_id}"
    payload = json.dumps({"id": player_id})
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text

def add_new_player(data):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/players"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
