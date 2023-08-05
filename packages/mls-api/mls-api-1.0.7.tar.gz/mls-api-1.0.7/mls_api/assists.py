import requests
import json

def get_all_assists():
    url = "https://mlssoccerapi.com/assists"
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def get_assist_by_id(assist_id):
    url = f"https://mlssoccerapi.com/assists/{assist_id}"
    payload = {}
    headers = {'Content-Type': 'application/json'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def update_assist_by_id(assist_id, league_name, standing, player_name, team_name, assists, tag):
    url = f"https://mlssoccerapi.com/assists/{assist_id}"
    payload = json.dumps({
        "id": assist_id,
        "league_name": league_name,
        "standing": standing,
        "player_name": player_name,
        "team_name": team_name,
        "assists": assists,
        "tag": tag
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text


def delete_assist_by_id(assist_id):
    url = f"https://mlssoccerapi.com/assists/{assist_id}"
    payload = json.dumps({"id": assist_id})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text


def add_new_assist(assist_id, league_name, standing, player_name, team_name, assists, tag):
    url = "https://mlssoccerapi.com/assists"
    payload = json.dumps({
        "id": assist_id,
        "league_name": league_name,
        "standing": standing,
        "player_name": player_name,
        "team_name": team_name,
        "assists": assists,
        "tag": tag
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
