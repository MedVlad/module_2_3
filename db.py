import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
""")
connection.commit()

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email on Users (email)")
data = ("newuser", "wer@mail.ru", 28)
cursor.execute("INSERT INTO Users(username,email,age) VALUES(?,?,?)", data)


connection.commit()
connection.close()
