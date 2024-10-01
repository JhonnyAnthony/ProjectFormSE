from msal import ConfidentialClientApplication
import requests
import os
from dotenv import load_dotenv

load_dotenv()
form_id = os.getenv("MY_FORM_ID")
tenant_id = os.getenv("MY_TENANT_ID")
url = f'https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={form_id}'

app = ConfidentialClientApplication(
    authority=f"https://login.microsoftonline.com/{tenant_id}",
    client_id=os.getenv("MY_CLIENT_ID"),
    client_credential=os.getenv("MY_CLIENT_SECRET")
)

result = app.acquire_token_by_username_password(
    username=os.getenv("MY_USERNAME"),
    password=os.getenv("MY_PASSWORD"),
    scopes=["Forms.Read.All", "Forms.Read", "Response.Read.All"]
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
        print(f"https://login.microsoftonline.com/{tenant_id}/adminconsent?client_id={os.getenv('MY_CLIENT_ID')}")
