import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore

def create_database():
    try: 
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root"
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error connetion to mysql: {e}")

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("mysql connection closed")