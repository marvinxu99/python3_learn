import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users
        (User_Id INT, First_Name TEXT, Last_Name TEXT, Email TEXT)''')

user_list = [
    (1, 'Quentin', 'Tarantino', 'qt@gamil.com'),
    (2, 'Steven', 'Spielberg', 'steven@gamil.com'),
    (3, 'West', 'Anderson', 'west@gail.com')
]

# if len(user_list):
#     query = 'INSERT INTO Users VALUES (?,?,?,?)'
#     cursor.executemany(query, user_list)

cursor.execute("SELECT * FROM Users")
records = cursor.fetchall()
for record in records:
     print(record)

# # Filter
print("Filter...")
cursor.execute("SELECT Email FROM Users")
print(cursor.fetchall())

connection.commit()
connection.close()
