import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class LoginAutomation:
    def __init__(self, email, password, form_id, download_dir):
        self.email = email
        self.password = password
        self.form_id = form_id
        self.download_dir = download_dir

        # Set up Chrome options to specify the download directory and disable cache and cookies        
        chrome_options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(options=chrome_options)

    def login_and_download(self):
        # Open the login page
        self.driver.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=c9a559d2-7aab-4f13-a6ed-e7e9c52aec87&redirect_uri=https%3A%2F%2Fforms.office.com%2Flanding&state=eyJ2ZXJzaW9uIjoxLCJkYXRhIjp7InByb21wdCI6IkFjNThBdEJrTHZub2o0eHI5aG12MVBwWFhJdU1hMGxHcXdYUWlWRXIwSl9Fc1kyUE9TdmFfYWthSTJ0VlRmeENOaU5aUzhQSlhPcXhZYm9XeUNSUWk2dyIsIi5yZWRpcmVjdCI6Imh0dHBzOi8vZm9ybXMub2ZmaWNlLmNvbS9QYWdlcy9EZXNpZ25QYWdlLmFzcHg_b3JpZ2luPU1hcmtldGluZyIsIi54c3JmIjoiQWViN1cwbV9ENk9MUjY1Y3dHeTJkWm5XZmV6eGFTdVB1UnNEQTg3eHMxR1dac21OVFVNcDFtUHhhRHpFa2RWLUdCM2djQXFMb29UeFBTT0dzOFF1b2Y2NmllZ2JuRnlHRVdmWThfX2RoSU1adG1iQU5PUHZjblVPTEhSdmRXb01ndyIsIk9wZW5JZENvbm5lY3QuQ29kZS5SZWRpcmVjdFVyaSI6IkFlOU42REd5MVJPbkpnMG9rd2FnNmZxdjBmR1gxMDE1dlFKMGtRcEh4OEU4ZjY4RzMtZUpGN1lvVGhUMk43bUExY1BzLVR0X2tWcjhTenRKYnJrM2xWSk9ueDNoZUhZNXFhcnk3MVIxM1NtMHJ1VzZ3Ny1QaFZXV1BVdmFWejdLYncifX0&response_type=code%20id_token&scope=openid%20profile&response_mode=form_post&nonce=638633864343783628.NjgwM2Y1NzctZmM4My00NzNmLWFlMmEtMzEzY2NjMjQyMWU1YmYwNzBmZmYtMjA4OS00M2IzLWJiZmItNzQ5MzFlOGU2MTcw&prompt=select_account&x-client-SKU=ID_NET8_0&x-client-ver=7.2.0.0')
        try:
            # Wait for the email input field to be present
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))
            )
            # Enter your email
            email_field.send_keys(self.email + Keys.RETURN)
            # Wait for the password input field to be present
            password_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="i0118"]'))
            )
            # Enter your password and send Enter key
            password_field.send_keys(self.password + Keys.RETURN) 
            print("chegou aqui")
            # Wait for the submit button to be present
            # Wait for a few seconds to ensure the login process completes
            time.sleep(5)
            # Navigate to another link
            download_url = f'https://forms.office.com/formapi/DownloadExcelFile.ashx?formid={self.form_id}&Token=18e6819de29249d68f1ef46c143015fd'
            self.driver.get(download_url)
            
        except selenium.common.exceptions.NoSuchElementException:
            print("Element not found")
        finally:
            # Close the browser after a few seconds
            time.sleep(15)
            self.driver.quit()

# Example usage
