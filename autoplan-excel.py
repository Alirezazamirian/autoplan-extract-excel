import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# Example of using the parameters (e.g., connecting to a PostgreSQL database)
try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    print("Connected to the database.")

    # Your code to interact with the database goes here

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")
