import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")

cursor.execute('''CREATE TABLE IF NOT EXISTS Users
        (User_Id INTEGER PRIMARY KEY AUTOINCREMENT, 
            First_Name TEXT, Last_Name TEXT, Email TEXT)''')

user_list = [
    ('Quentin', 'Tarantino', 'qt@gamil.com'),
    ('Steven', 'Spielberg', 'steven@gamil.com'),
    ('West', 'Anderson', 'west@gail.com')
]

if len(user_list):
    query = 'INSERT INTO Users(First_Name,Last_Name,Email) VALUES(?,?,?)'
    cursor.executemany(query, user_list)

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
