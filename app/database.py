import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="loja",
        user="postgres",
        password="30abril01",
        port=5432
    )