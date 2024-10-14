from msgraph import api
import os

authority_host_uri = 'https://login.microsoftonline.com'
tenant = 'e220d369-e6a8-4126-83ef-b4b6bbfd9367'
resource_uri = 'https://graph.microsoft.com'
client_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
client_secret = 'rpz8Q~H1srxTSMPgaRUVvtKnHkCz1SnmwpN5zb~H'
api_instance = api.GraphAPI.from_certificate(authority_host_uri, tenant, resource_uri, client_id,)



