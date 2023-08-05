import requests
import json

BASE_URL = "https://mlssoccerapi.com/teams"

headers = {
    'Content-Type': 'application/json'
}

def get_all_teams():
    response = requests.get(BASE_URL, headers=headers)
    return response.text

def get_team_by_id(team_id):
    url = f"{BASE_URL}/{team_id}"
    response = requests.get(url, headers=headers)
    return response.text

def update_team_by_id(team_id, data):
    url = f"{BASE_URL}/{team_id}"
    payload = json.dumps(data)
    response = requests.put(url, headers=headers, data=payload)
    return response.text

def delete_team_by_id(team_id):
    url = f"{BASE_URL}/{team_id}"
    response = requests.delete(url, headers=headers)
    return response.text

def add_new_team(data):
    payload = json.dumps(data)
    response = requests.post(BASE_URL, headers=headers, data=payload)
    return response.text
