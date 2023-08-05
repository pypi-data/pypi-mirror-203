import os, json
import requests

def get_all_topscorers():
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/topscorer"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def get_topscorer_by_id(topscorer_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/topscorer/{topscorer_id}"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def update_topscorer_by_id(topscorer_id, league_name, standing, player_name, team_name, goals, tag):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/topscorer/{topscorer_id}"
    payload = json.dumps({
        "id": topscorer_id,
        "league_name": league_name,
        "standing": standing,
        "player_name": player_name,
        "team_name": team_name,
        "goals": goals,
        "tag": tag
    })
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text


def delete_topscorer_by_id(topscorer_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/topscorer/{topscorer_id}"
    payload = json.dumps({"id": topscorer_id})
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text


def add_new_topscorer(topscorer_id, league_name, standing, player_name, team_name, goals, tag):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/topscorer"
    payload = json.dumps({
        "id": topscorer_id,
        "league_name": league_name,
        "standing": standing,
        "player_name": player_name,
        "team_name": team_name,
        "goals": goals,
        "tag": tag
    })
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
