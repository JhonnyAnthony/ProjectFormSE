from msal import ConfidentialClientApplication
import requests
import os
from dotenv import load_dotenv, dotenv_values
#Ids to variables  
load_dotenv()
form_id = os.getenv("MY_FORM_ID")
tenant_id = os.getenv("MY_TENANT_ID")
url = f'https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={form_id}'
# Initialize the ConfidentialClientApplication
load_dotenv()
app = ConfidentialClientApplication(
    authority= f"https://login.microsoftonline.com/{tenant_id}",
    client_id = os.getenv("MY_CLIENT_ID"),
    client_credential= os.getenv("MY_CLIENT_SECRET")  # client secret here
)

# Acquire token by username and password
load_dotenv()
result = app.acquire_token_by_username_password(
    username= os.getenv("MY_USERNAME"),
    password= os.getenv("MY_PASSWORD"),
    scopes=["Files.Read.All"]
)

# Check if the token was acquired successfully
if "access_token" in result:
    print("Access token:", result["access_token"])
    access_token = result["access_token"]
    # Set up the headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)

# Check the response
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.text)
    
else:
    print("Error:", result.get("error"), result.get("error_description"))
