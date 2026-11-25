import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

myDBConnection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  passwd=os.getenv("DB_PASSWORD")
)

print(myDBConnection)

db_name = "python_test_db"

mycursor = myDBConnection.cursor()

sqlquery = " CREATE DATABASE " + db_name

mycursor.execute(sqlquery)