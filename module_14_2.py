import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")
l = []

for i in range(1, 11):
    l.append(i)
    data = (f"User{i}", f"example{i}@gmail.com", i * 10, 1000)
    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)", data)
for i in l[0::2]:
    data = (f"User{i}",)
    cursor.execute("UPDATE Users SET balance = 500  WHERE username = ? ", data)
for i in l[::3]:
    data = (f"User{i}",)
    cursor.execute("DELETE FROM Users WHERE username = ? ", data)
data = (60,)

cursor.execute("SELECT username,email,age,balance FROM Users WHERE age <> ? ", data)
users = cursor.fetchall()

data = (6,)
cursor.execute("DELETE FROM Users WHERE id = ? ", data)

cursor.execute("SELECT COUNT(username) FROM Users ")
UserCount = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users ")
SumBalance = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users ")
AvgBalance = cursor.fetchone()[0]

print(SumBalance/UserCount)
print(AvgBalance)


for user in users:
    print(f"Имя:{user[0]}|Почта:{user[1]}|Возраст:{user[2]}|Баланс:{user[3]}")

connection.commit()
connection.close()
