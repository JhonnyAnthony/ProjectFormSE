from msal import PublicClientApplication
import requests
import os
from dotenv import load_dotenv

class ExcelDownloader:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("MY_CLIENT_ID")
        self.tenant_id = os.getenv("MY_TENANT_ID")
        self.client_secret = os.getenv("MY_CLIENT_SECRET")
        self.form_id = os.getenv("MY_FORM_ID")
        self.redirect_uri = "http://localhost"
        self.scopes = ["https://graph.microsoft.com/.default"]
        self.username = os.getenv("MY_USERNAME")
        self.password = os.getenv("MY_PASSWORD")

    def permission(self):
        # URL de autorização
        authorization_url = (
            f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/authorize"
            f"?client_id={self.client_id}"
            f"&response_type=code"
            f"&redirect_uri={self.redirect_uri}"
            f"&response_mode=query"
            f"&scope={' '.join(self.scopes)}"
            f"&state=12345"
        )

        print("Por favor, acesse a seguinte URL para conceder permissões:")
        print(authorization_url)

    def get_token(self):
        try:
            # Configuração do aplicativo público
            app = PublicClientApplication(
                self.client_id,
                authority=f"https://login.microsoftonline.com/{self.tenant_id}"
            )

            # Obtenção do token de acesso em nome do usuário
            result = app.acquire_token_by_username_password(
                username=self.username,
                password=self.password,
                scopes=self.scopes
            )

            if "access_token" in result:
                return result['access_token']
            else:
                raise Exception(f"Falha ao obter o token de acesso: {result.get('error_description', 'Erro desconhecido')}")
        except Exception as e:
            raise Exception(f"Erro ao obter o token de acesso: {str(e)}")

    def download_excel_file(self):
        url = f"https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={self.form_id}&timezoneOffset=180&__TimezoneId=America/Sao_Paulo&minResponseId=1&maxResponseId=2"
        try:
            access_token = self.get_token()
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                with open("Entrevista de Desligamento.xlsx", "wb") as file:
                    file.write(response.content)
                print("Arquivo baixado com sucesso!")
            else:
                print(f"Falha ao baixar o arquivo: {response.status_code}")
                print(response.text)  # Adiciona esta linha para ver a mensagem de erro detalhada
        except Exception as e:
            print(f"Erro: {str(e)}")

# Uso da classe
downloader = ExcelDownloader()

# Primeiro, gere a URL de autorização e peça ao usuário para conceder permissões

# Depois que o usuário conceder permissões, capture o código de autorização da URL de redirecionamento e passe para a função download_excel_file
auth_code = "0.AVkAadMg4qjmJkGD77S2u_2TZ9kPOWCdU5RLtZVrfVq1f0hZADM.AgABBAIAAADW6jl31mB3T7ugrWTT8pFeAwDs_wUA9P_cGdY-an-45uhE9iMqi7RiACGDaVSH1QgBURYB-tn-3X9o8EENFZ_mMXWWpdtZQJyB7uJx8DRDTbihUZbuXtrt2QCgc8BoMBymW01ojo1nhi9Y22pCFshythfyOs5l4RRmgIVnTGjt7IBf2FXNUF5aV4_BFOsj2RYxpmXDdWmkfwvfDQlENQSBf_6324Hprz3vYUxd8guTdDCrs8wuVwhnx_SU0HJGMcLOC87lEMFfHOb2ZXK2AVboKDa5Muvd6rnb4pN5SL0Pnslq8hY38ouC-Sw00hG5AFnYs4wCF3MfYz5uI3-IGzuKLnceoCEZ7tBd5Eho1bELCORJlQ63_iGv2hdx_uiOAzOOth4HJh6B3M5vU__l3ARD9S3ExJBpr-lockxqY6i6pfrt7EHdHR50NC4GdKkwcB9T-SYFTyW1zQaTBz_hFElS-G6ieHLjtl9C2lDFtUAVcJFv-lg5xwtM6RbFh6xRoJAVuMXasxHqNnDCThVzQ-62EplbvmNSNXYHxLugAkJUoX4MHokS-8_i2BONIeF3eU29S253clL4IWTFPN4tSa7nWcOykse2aUoXYmkthwVkUFHHFvRNJC5R_bbxc2D5Npytw7lws5GvDsGyYIU9__KbaThNdxGDKKyLqO8C6YKd-lPsvASD19ZbBa3u0L9WYuVKxgpDSmEW5tRmKNmEaFoAepd7y0ky3aXIU5lj4U4GNobglJ8XLkqEWMT6BHlQY88IUXsIHs846jbFV3sEMOQJPQwTEllEjaa_Lclpjn1Q_w7koI_9LC07JVSazYQiVNDEuwJYiucEr_kgYFv6cSrKq99M"
downloader.download_excel_file()
