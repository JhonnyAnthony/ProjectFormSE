import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'venv', '.env')
load_dotenv(dotenv_path)

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USER')
sheet = os.getenv("SHEET")
file_name = os.getenv("FILE_NAME")
password = os.getenv('DB_PASSWORD')
client_id = os.getenv("MY_CLIENT_ID")
client_secret = os.getenv("MY_CLIENT_SECRET")
tenant_id = os.getenv("MY_TENANT_ID")
link = os.getenv("LINK_AUTHORITY")
authority = f"{link}{tenant_id}"
api_id = os.getenv("MY_API_ID")
url = os.getenv("MY_URL")
process_id = os.getenv("PROCESS_ID")
user = os.getenv("MY_USER")
