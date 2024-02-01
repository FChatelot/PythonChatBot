import psycopg2 
from dotenv import load_dotenv
import os
load_dotenv()
def db_conn():
    url = os.environ.get("POSTGREURL")
    conn = psycopg2.connect(url)
    return conn
conn = db_conn()
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name varchar(100), description varchar(100), email varchar(255));''')    

conn.commit()
cursor.close()
conn.close()
    