# Import the required MySQL library and error handler
import mysql.connector
from mysql.connector import Error

# Attempt to connect to the MySQL server and create a new database 
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ulrich',
        database = 'alx_book_store'
    )

    # If the connection is successful, create the database , and if only the database doesnot exist
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

# If an error occurs while connecting, print the error message and explain the error as e
except Error as e:
    print(f"Error while connecting to MySQL: {e}")
try:
        cursor.execute("USE alx_book_store")

                # Step 4: Create authors table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Authors (
                    author_id INT PRIMARY KEY,
                    author_name VARCHAR(215)
                )
                """)

                # Step 5: Create books table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Books (
                    book_id INT PRIMARY KEY,
                    title VARCHAR(130),
                    author_id INT,
                    price DOUBLE,
                    publication_date DATE,
                    FOREIGN KEY (author_id) REFERENCES authors(author_id)
                  
                )
                """)

                # Step 6: Create customers table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                    customer_id INT PRIMARY KEY,
                    customer_name VARCHAR(215),
                    email VARCHAR(215),
                    address TEXT
                )
                """)

                # Step 7: Create orders table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    order_id INT PRIMARY KEY,
                    customer_id INT,
                    order_date DATE,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                )
                """)

                # Step 8: Create order_details table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS Order_details (
                    orderdetailid INT PRIMARY KEY,
                    order_id INT,
                    book_id INT,
                    quantity DOUBLE,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                    FOREIGN KEY (book_id) REFERENCES Books(book_id)
                )
                """)
        

        print("All tables created successfully!")
      
except Error as e:      
    print("Error:", e)

finally:
    # Step 9: Close connection and print out all table in
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        for tables in cursor:
             print([tables])
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection closed.")



    

