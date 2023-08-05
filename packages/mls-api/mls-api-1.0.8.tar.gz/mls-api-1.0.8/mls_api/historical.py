import os, json
import requests

def get_all_hist():
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/hist"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def get_hist_by_id(hist_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/hist/{hist_id}"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def update_hist_by_id(hist_id, data):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/hist/{hist_id}"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text

def delete_hist_by_id(hist_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/hist/{hist_id}"
    payload = json.dumps({"id": hist_id})
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text

def add_new_hist(data):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/hist"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
