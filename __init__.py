import os
import requests
from azure.identity import  AzureCliCredential

# DefaultAzureCredential, InteractiveBrowserCredential,
# cred = InteractiveBrowserCredential()

# Use one of these credential objects to get an access token
cred = AzureCliCredential() # i.e. `az login`

# Request an access token with the following scope
scope = "https://forms.office.com/.default"

tok = cred.get_token(scope)
print(tok)
# print(type(tok))

formid = os.getenv("adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u")
tenantid = os.getenv("e220d369-e6a8-4126-83ef-b4b6bbfd9367")
userid = os.getenv("d602bd3e-6752-4b4a-9dc0-c7ab6020f2d3")

url = f"https://forms.office.com/formapi/api/{tenantid}/users/{userid}/light/forms('{formid}')/responses?$expand=comments&$top=7&$skip=0"
# print(url)

# Provide the access token in the request header
headers = {"Authorization": f"Bearer {tok.token}"}

r = requests.get(url, headers=headers)
print(r.json())