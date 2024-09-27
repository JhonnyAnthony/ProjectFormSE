import webbrowser
import requests
from msal import ConfidentialClientApplication

tenant_id = 'e220d369-e6a8-4126-83ef-b4b6bbfd9367'
client_secret = 'nxj8Q~l5Ym799LxBI0xIzpJ3LF4oY8mQRuXV4a7q'
app_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
SCOPES = ['User.Read']

client = ConfidentialClientApplication (client_id=app_id, client_credential=client_secret)
authorization_url = client.get_authorization_request_url(SCOPES)
print(authorization_url)
webbrowser.open(authorization_url)

def token():
    # Get access token
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': app_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()  # Add error handling
    access_token = response.json().get('access_token')
    print(access_token)
    access_id = access_token['acess_token']
token()