import os
from dotenv import load_dotenv
import msal
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)

client_id = os.getenv("MY_CLIENT_ID")
client_secret = os.getenv("MY_CLIENT_SECRET")
tenant_id = os.getenv("MY_TENANT_ID")
authority = f"https://login.microsoftonline.com/{tenant_id}"

class IntegrationOneDrive:
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
        url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
        payload = {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'scope': 'https://graph.microsoft.com/.default'
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()
        access_token = response.json().get('access_token')
        # print(access_token)
        return access_token

    def download(self):
        access_token = self.get_token()
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        drive_id = os.getenv("MY_DRIVE_ID")
        item_id = os.getenv("MY_ITEM_ID")

        response = requests.get(f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{item_id}", headers=headers)

        
        if response.status_code == 403:
            print("Error 403: Forbidden. You do not have permission to access this resource.")
            print(response.text)
        elif response.status_code == 404:
            print("Error 404: Not Found. The resource could not be found.")
            print(response.text)
        elif response.status_code == 200:
            item_details = response.json()
            # print(f"Item Details: {item_details}")
            download_url = item_details.get('@microsoft.graph.downloadUrl')
            if download_url:
                file_response = requests.get(download_url)
                with open('Entrevista de Desligamento.xlsx', 'wb') as f:

                    f.write(file_response.content)
                print("File downloaded successfully.")
            else:
                print("Download URL not found.")
        else:
            print(f"Error {response.status_code}: {response.text}")

