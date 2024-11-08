import sqlite3


def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT ,
    price INTEGER NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def is_included(username):
    result = False
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    data = (username,)
    cursor.execute("SELECT COUNT(username) FROM Users WHERE username = ? ", data)
    is_present = cursor.fetchone()[0]
    if is_present > 0:
        result = True
    return result


def add_user(username, email, age):
    #if is_included(username):
     #   return
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    data = (username, email, age, 1000)
    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)", data)
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products ")
    products = cursor.fetchall()

    return products
