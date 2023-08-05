import os, json
import requests

def get_all_offence():
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/offence"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def get_offence_by_id(offence_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/offence/{offence_id}"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def update_offence_by_id(offence_id, league_name, standing, player_name, team_name, yellow_cards, red_cards, tag):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/offence/{offence_id}"
    payload = json.dumps({
        "id": offence_id,
        "league_name": league_name,
        "standing": standing,
        "player_name": player_name,
        "team_name": team_name,
        "yellow_cards": yellow_cards,
        "red_cards": red_cards,
        "tag": tag
    })
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text


def delete_offence_by_id(offence_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/offence/{offence_id}"
    payload = json.dumps({"id": offence_id})
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text


def add_new_offence(offence_id, league_name, standing, player_name, team_name, yellow_cards, red_cards, tag):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/offence"
    payload = json.dumps({
        "id": offence_id,
        "league_name": league_name,
        "standing": standing,
        "player_name": player_name,
        "team_name": team_name,
        "yellow_cards": yellow_cards,
        "red_cards": red_cards,
        "tag": tag
    })
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
