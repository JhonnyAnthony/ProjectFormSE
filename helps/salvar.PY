
# # import requests
# # import webbrowser
# # from msal import ConfidentialClientApplication

# # # Replace these variables with your actual values
# # tenant_id = 'e220d369-e6a8-4126-83ef-b4b6bbfd9367'
# # form_id = 'adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u'
# # user_id = 'd602bd3e-6752-4b4a-9dc0-c7ab6020f2d3'
# # client_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
# # client_secret = 'nxj8Q~l5Ym799LxBI0xIzpJ3LF4oY8mQRuXV4a7q'
# # SCOPE = ["User.ReadBasic.All"]
# # def main():
# #     # Get token and fetch form responses
# #     access_token = get_token()

# #     # Authorization URL for further actions if needed

# # def get_token():
# #     # Get access token
# #     url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

# #     payload = {
# #         'grant_type': 'client_credentials',
# #         'client_id': client_id,
# #         'client_secret': client_secret,
# #         'scope': 'https://graph.microsoft.com/.default'
# #     }
# #     response = requests.post(url, data=payload)
# #     access_token = response.json().get('access_token')
# #     print(access_token)
# #     return access_token


# # main()
# import requests
# import webbrowser
# from msal import ConfidentialClientApplication

# # Replace these variables with your actual values
# tenant_id = 'e220d369-e6a8-4126-83ef-b4b6bbfd9367'
# form_id = 'adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u'
# user_id = 'd602bd3e-6752-4b4a-9dc0-c7ab6020f2d3'
# client_id = '60390fd9-539d-4b94-b595-6b7d5ab57f48'
# client_secret = 'nxj8Q~l5Ym799LxBI0xIzpJ3LF4oY8mQRuXV4a7q'
# SCOPE = ["User.ReadBasic.All"]
# def main():
#     # Get token and fetch form responses
#     access_token = get_token()

#     # Authorization URL for further actions if needed

# def get_token():
#     # Get access token
#     url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

#     payload = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'scope': 'https://graph.microsoft.com/.default'
#     }
#     response = requests.post(url, data=payload)
#     access_token = response.json().get('access_token')
#     print(access_token)
#     return access_token


# main()
