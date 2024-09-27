import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

app_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
SCOPES = ['User.Read']

client = PublicClientApplication(client_id=app_id)

flow = client.initiate_device_flow(scopes=SCOPES)
print(flow)