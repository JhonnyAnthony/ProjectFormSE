import os
from dotenv import load_dotenv
import pyodbc

# Load environment variables from .env file
load_dotenv()

# Retrieve the variables
server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

# Connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the database
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Create a cursor
    cursor = conn.cursor()

    # Example query
    cursor.execute("SELECT * FROM your_table_name")

    # Fetch and print all rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
