import requests
import json

def login(username, password):
    url = "https://mlssoccerapi.com/v1/login"
    payload = json.dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)

def auth_header(login_response):
    return {
        'Authorization': f'Bearer {login_response["token"]}'
    }
