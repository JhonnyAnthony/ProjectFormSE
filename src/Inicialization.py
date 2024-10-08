from login_automation import LoginAutomation
import os
from dotenv import load_dotenv
load_dotenv()
email = os.getenv("MY_USERNAME")
password = os.getenv("MY_PASSWORD")
form_id = 'adMg4qjmJkGD77S2u_2TZz69AtZSZ0pLncDHq2Ag8tNUM1ZBQkFZVUFCMEYyNEM0SDJFNUhUTDZBUS4u'
download_dir = 'C:\\Users\\jhonny.souza\\Downloads'
automation = LoginAutomation(email, password, form_id, download_dir)
automation.login_and_download()