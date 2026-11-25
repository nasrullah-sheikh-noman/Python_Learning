import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_name = "python_test_db"

myDBConnection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  passwd=os.getenv("DB_PASSWORD"),
  database=db_name
)

myCursor = myDBConnection.cursor()

sqlQuery = """
              UPDATE STUDENT
              SET NAME = "Nasrullah sheikh noman"
              WHERE NAME = "Noman"
            """

myCursor.execute(sqlQuery)
myDBConnection.commit()

print("update data in table")