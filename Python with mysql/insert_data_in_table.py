import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_name = "python_test_db"

myDBConnection = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_user"),
  passwd=os.getenv("DB_PASSWORD"),
  database=db_name
)

myCursor = myDBConnection.cursor()

sqlQuery = """
              INSERT INTO STUDENT(
                ROLL, NAME, DEPT, UNIVERSITY
              )
              VALUES
                  ("1243", "Noman", "CSE", "IUT"),
                  ("3423", "Nasrullah", "CS", "SUST")
            """

myCursor.execute(sqlQuery)
myDBConnection.commit()

print("Insert data into table")