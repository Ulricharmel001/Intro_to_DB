import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'ulrich'
        )
    print("Connected to  DB successfully")
except Exception as e:
    print(f'Unable to connect to DB {e}')
mycursor = mydb.cursor()
try:
        mycursor.execute("USE alx_book_store")

                # Step 4: Create authors table
        mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Authors (
                    author_id INT PRIMARY KEY,
                    author_name VARCHAR(215)
                )
                """)

                # Step 5: Create books table
        mycursor.execute("""
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
        mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                    customer_id INT PRIMARY KEY,
                    customer_name VARCHAR(215),
                    email VARCHAR(215),
                    address TEXT
                )
                """)

                # Step 7: Create orders table
        mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    order_id INT PRIMARY KEY,
                    customer_id INT,
                    order_date DATE,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                )
                """)

                # Step 8: Create order_details table
        mycursor.execute("""
                CREATE TABLE IF NOT EXISTS Order_Details (
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
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("SHOW TABLES")
        for tables in cursor:
             print([tables])
        mydb.commit()
        cursor.close()
        mydb.close()
        print("MySQL connection closed.")

