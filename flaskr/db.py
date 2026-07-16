import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()

database = os.getenv('DATABASE')
host = os.getenv('HOST')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

def get_connection():
    connection = psycopg2.connect(
        dbname=database,
        host=host,
        user=username,
        password=password,
        port=5432,
        connect_timeout=5
    )
    return connection



