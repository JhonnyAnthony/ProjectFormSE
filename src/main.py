import requests
import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

# Replace these variables with your actual values

tenant_id = 'e220d369-e6a8-4126-83ef-b4b6bbfd9367'
form_id = 'adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u'
user_id = 'd602bd3e-6752-4b4a-9dc0-c7ab6020f2d3'

client_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
client_secret = 'nxj8Q~l5Ym799LxBI0xIzpJ3LF4oY8mQRuXV4a7q'
SCOPE = ["User.ReadBasic.All"]

def token():
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
    print(access_token)
    login()

def forms_call():
    # Fetch form responses
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    url = f"https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={form_id}"
    response2 = requests.get(url, headers=headers)
    form_responses = response2.json()

    print(form_responses)

def login():
    # Technically we could use empty list [] as scopes to do just sign in,
    # here we choose to also collect end user consent upfront
    session = _build_auth_code_flow(scopes=SCOPE)
    print(session)
    forms_call()
    # return render_template("login.html", auth_url=session["flow"]["auth_uri"], version=msal.__version__)

def _build_msal_app(cache=None, authority=None):
    return msal.ConfidentialClientApplication(
        client_id.CLIENT_ID, authority=authority or client_id.AUTHORITY,
        client_credential=client_id.CLIENT_SECRET, token_cache=cache)

def _build_auth_code_flow(authority=None, scopes=None):
    return _build_msal_app(authority=authority).initiate_auth_code_flow(
        scopes or [],
        redirect_uri=url_for("authorized", _external=True)) 
token()        