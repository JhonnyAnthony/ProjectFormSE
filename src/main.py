from msal import ConfidentialClientApplication
import requests
import os
from dotenv import load_dotenv

load_dotenv()
form_id = os.getenv("MY_FORM_ID")
url = f'https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={os.getenv("MY_FORM_ID")}'

app = ConfidentialClientApplication(
    authority="https://login.microsoftonline.com/e220d369-e6a8-4126-83ef-b4b6bbfd9367",
    client_id=os.getenv("MY_CLIENT_ID"),
    client_credential=os.getenv("MY_CLIENT_SECRET")
)

result = app.acquire_token_by_username_password(
    username=os.getenv("MY_USERNAME"),
    password=os.getenv("MY_PASSWORD"),
    scopes=["Forms.Read.All"]
)

if "access_token" in result:
    access_token = result["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)
else:
    print("Error:", result.get("error"), result.get("error_description"))
    if result.get("error") == "invalid_grant":
        print("Please visit the following URL to grant consent:")
        print(f"https://forms.office.com/formapi/DownloadExcelFile.ashx?formid=adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u&timezoneOffset=180&__TimezoneId=America/Sao_Paulo&minResponseId=1&maxResponseId=1")
