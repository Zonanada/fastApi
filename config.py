from dotenv import load_dotenv, find_dotenv
from os import getenv

load_dotenv(find_dotenv())

DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")
