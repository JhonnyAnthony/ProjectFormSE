from msal import ConfidentialClientApplication
import requests
import os
from dotenv import load_dotenv

class ExcelDownloader:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("MY_CLIENT_ID")
        self.tenant_id = os.getenv("MY_TENANT_ID")
        self.form_id = os.getenv("MY_FORM_ID")
        self.client_secret = os.getenv("MY_CLIENT_SECRET")
        self.redirect_uri = "http://localhost:60865"
        self.scopes = ["https://graph.microsoft.com/.default"]

    def get_authorization_url(self):
        app = ConfidentialClientApplication(self.client_id, authority=f"https://login.microsoftonline.com/{self.tenant_id}")
        authorization_url = app.get_authorization_request_url(self.scopes, redirect_uri=self.redirect_uri)
        print("Acesse esta URL para obter o código de autorização:", authorization_url)

    def get_token(self, auth_code):
        app = ConfidentialClientApplication(
            self.client_id,
            authority=f"https://login.microsoftonline.com/{self.tenant_id}",
            client_credential=self.client_secret
        )

        result = app.acquire_token_by_authorization_code(auth_code, scopes=self.scopes, redirect_uri=self.redirect_uri)

        if "access_token" in result:
            return result['access_token']
        else:
            raise Exception(f"Falha ao obter o token de acesso: {result.get('error_description', 'Erro desconhecido')}")

    def download_excel_file(self, access_token):
        url = f"https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={self.form_id}&timezoneOffset=180&__TimezoneId=America/Sao_Paulo&minResponseId=1&maxResponseId=2"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            with open("Entrevista de Desligamento.xlsx", "wb") as file:
                file.write(response.content)
            print("Arquivo baixado com sucesso!")
        else:
            print(f"Falha ao baixar o arquivo: {response.status_code}")
            print(response.text)

# Uso da classe
downloader = ExcelDownloader()

# Passo 1: Gere a URL de autorização
downloader.get_authorization_url()

# O usuário deve acessar a URL, conceder permissões e obter o código de autorização.
auth_code = input("Cole o código de autorização aqui: ")  # Permita que o usuário insira o código

# Passo 2: Obtenha o token e faça o download
try:
    access_token = downloader.get_token(auth_code)  # Passa o código de autorização
    downloader.download_excel_file(access_token)
except Exception as e:
    print(f"Erro: {str(e)}")
