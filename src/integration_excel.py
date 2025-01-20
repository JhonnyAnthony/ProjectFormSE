import os
from config import client_id,client_secret,tenant_id,authority
import msal
import requests
import logging

class IntegrationOneDrive: #here is to declare token requirements
    def __init__(self, client_id, client_secret, authority):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authority = authority
        self.app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            authority=self.authority,
            client_credential=self.client_secret,
        )
    #Here is where get token
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
        return access_token
    #Here is where the download happes
    def download(self):
        access_token = self.get_token()
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        drive_id = os.getenv("MY_DRIVE_ID")
        item_id = os.getenv("MY_ITEM_ID")
        # Search for the item on graphs using drive_id and item_id
        response = requests.get(f"https://graph.microsoft.com/v1.0/drives/{drive_id}/items/{item_id}", headers=headers)

        if response.status_code == 200:
            item_details = response.json()
            #Here is where the download happes, when the response get the item it gonna search to download url
            download_url = item_details.get('@microsoft.graph.downloadUrl')
            if download_url:
                file_response = requests.get(download_url)
                with open('Entrevista de Desligamento.xlsx', 'wb') as f:
                    f.write(file_response.content)
                logging.info(f"File downloaded successfully.{response.status_code}")
            else:
                logging.error(f"Download URL not found.{response.status_code}:{response.text}")
        #If has a error print error code and text
        else:
            logging.error(f"Error {response.status_code}: {response.text} - Integration_Excel")
