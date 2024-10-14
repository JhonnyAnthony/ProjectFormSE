import os
from dotenv import load_dotenv
import msal
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '..','src', 'venv', '.env')
load_dotenv(dotenv_path)

client_id = os.getenv("MY_CLIENT_ID")
client_secret = os.getenv("MY_CLIENT_SECRET")
tenant_id = os.getenv("MY_TENANT_ID")
authority = f"https://login.microsoftonline.com/{tenant_id}"
redirect_uri = 'http://localhost:8080/'

class Integration_OneDrive:
    def __init__(self, client_id, client_secret, authority):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authority = authority
        self.app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            authority=self.authority,
            client_credential=self.client_secret,
        )

    def get_token(self):
        # Get access token
        url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        access_token = response.json().get('access_token')
        return access_token

    def main(self):
        # Get token and fetch form responses
        access_token = self.get_token()
        
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Use the access token to make requests to the Microsoft Graph API
        drive_id = os.getenv("MY_DRIVE_ID") 
        item_id = os.getenv("MY_ITEM_ID")
        response = requests.get(f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{item_id}/workbook/worksheets", headers=headers)

        
        if response.status_code == 404:
            print("Item not found. Please verify the item ID.")
        elif response.status_code == 403:
            print("Access denied. Please check your permissions.")
        else:
            response.raise_for_status()  # Raise an exception for other HTTP errors
            print(response.text)
            # Save the file locally
            with open('Entrevista de Desligamento 1.xlsx', 'wb') as f:
                f.write(response.content)

# Create an instance of the class and call the main method
integration = Integration_OneDrive(client_id, client_secret, authority)
integration.main()
