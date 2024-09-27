import requests
import webbrowser
from msal import ConfidentialClientApplication
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyring
import logging
from selenium.common.exceptions import WebDriverException

# Replace these variables with your actual values
tenant_id = 'e220d369-e6a8-4126-83ef-b4b6bbfd9367'
form_id = 'adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u'
user_id = 'd602bd3e-6752-4b4a-9dc0-c7ab6020f2d3'
client_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
client_secret = 'nxj8Q~l5Ym799LxBI0xIzpJ3LF4oY8mQRuXV4a7q'
SCOPE = ["User.ReadBasic.All"]

def get_token():
    # Get access token
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=payload)
    access_token = response.json().get('access_token')
    return access_token

def fetch_form_responses(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/drive/items/{form_id}/workbook/worksheets"
    response = requests.get(url, headers=headers)
    form_responses = response.json()

def main():
    # Get token and fetch form responses
    access_token = get_token()
    fetch_form_responses(access_token)

    # Authorization URL for further actions if needed

    client = ConfidentialClientApplication(client_id=client_id, client_credential=client_secret, authority=f"https://login.microsoftonline.com/{tenant_id}/")
    authorization_url = client.get_authorization_request_url(SCOPE)
    print(authorization_url)
    webbrowser.open(authorization_url)
    print("chegou aqui")
main()
