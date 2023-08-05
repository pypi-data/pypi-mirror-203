import os, json
import requests

def get_all_rtd():
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/rtd"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def get_rtd_by_id(rtd_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/rtd/{rtd_id}"
    payload = {}
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text

def update_rtd_by_id(rtd_id, data):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/rtd/{rtd_id}"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.text

def delete_rtd_by_id(rtd_id):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = f"https://mlssoccerapi.com/rtd/{rtd_id}"
    payload = json.dumps({"id": rtd_id})
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.text

def add_new_rtd(data):
    bearerToken = os.getenv('BEARER_TOKEN')
    url = "https://mlssoccerapi.com/rtd"
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {bearerToken}'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
