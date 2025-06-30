# import sql connector
import mysql.connector
from mysql.connector import Error
#connect my database and display error message if any one occur as {e}, diplay success message if conn succ
try:

    mydb = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password = "ulrich"
        )
    mycursor = mydb.cursor()
    print(f"connected successfully to Database")
except mysql.connector.Error:
    print(f"unable to connect to DB {e} ")

try:   # If the connection is successful, create the database , and if only the database doesnot exist
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

# If an error occurs while connecting, print the error message and explain the error as e
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
