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
              CREATE TABLE STUDENT(
                ROLL VARCHAR(8),
                NAME VARCHAR(50),
                DEPT VARCHAR(120),
                UNIVERSITY VARCHAR(220)
              )
            """

myCursor.execute(sqlQuery)

print("Create table sucessfull")