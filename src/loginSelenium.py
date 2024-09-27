# import requests
# import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import keyring
# import logging
# from selenium.common.exceptions import WebDriverException
# from msal import ConfidentialClientApplication, PublicClientApplication


# def login_and_click():
#     # Retrieve credentials
#     username = ""
#     password = ""
#     # Set up the WebDriver (make sure you have the appropriate driver installed)
#     driver = webdriver.Chrome()

#     try:
#         # Open the specified webpage
#         driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=8c59ead7-d703-4a27-9e55-c96a0054c8d2")

#         # Locate the username input field using XPath and send the username
#         username_field = driver.find_element(By.XPATH, '//*[@id="i0116"]')
#         username_field.send_keys(username)


#         # Locate the password input field using XPath and send the password
#         password_field = driver.find_element(By.XPATH, '//*[@id="i0118"]')
#         password_field.send_keys(password)

#         # Press Enter to submit the form
#         password_field.send_keys(Keys.RETURN)

#         # # Wait for the element to be clickable and then click it
#         # WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pt1:_UIScil1u"]'))).click()
#         # # Call the next function
#     finally:
#         # Close the browser
#         driver.quit()
