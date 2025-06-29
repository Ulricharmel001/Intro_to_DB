import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ulrich'
    )
    print("Connected to DB successfully")
except Error as e:
    print(f"Unable to connect to DB: {e}")
    exit()

mycursor = mydb.cursor()

try:
    # Use the database
    mycursor.execute("USE alx_book_store")

    # Create authors table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Authors (
            author_id INT PRIMARY KEY,
            author_name VARCHAR(215)
        )
    """)

    # Create books table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            book_id INT PRIMARY KEY,
            title VARCHAR(130),
            author_id INT,
            price DOUBLE,
            publication_date DATE,
            FOREIGN KEY (author_id) REFERENCES Authors(author_id)
        )
    """)

    # Create customers table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            customer_id INT PRIMARY KEY,
            customer_name VARCHAR(215),
            email VARCHAR(215),
            address TEXT
        )
    """)

    # Create orders table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INT PRIMARY KEY,
            customer_id INT,
            order_date DATE,
            FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
        )
    """)

    # Create order_details table
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
    # Show all tables
    if mydb.is_connected():
        mycursor.execute("SHOW TABLES")
        print("\nTables in 'alx_book_store':")
        for table in mycursor:
            print(table[0])
        mycursor.close()
        mydb.close()
        print("MySQL connection closed.")
