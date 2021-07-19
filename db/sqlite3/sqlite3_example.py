import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Movies")

cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
        (Title TEXT, Director TEXT, Year INT)''')

# cursor.execute("INSERT INTO Movies VALUES('Taxi Driver', 'Martin Scorsese', 1976)")

cursor.execute("SELECT * FROM Movies")
print(cursor.fetchone())

famous_films = [
    ('Pulp Fictin', 'Quentin Tarantino', 1994),
    ('Back to the Future', 'Steven Spielberg', 1985),
    ('Moonrise Kingdom', 'Wes Anderson', 2012)
]
cursor.executemany('INSERT INTO Movies VALUES (?,?,?)', famous_films)

cursor.execute("SELECT * FROM Movies")
records = cursor.fetchall()
print(type(records))
for record in records:
     print(record)

# Filter
print("Filter...")
release_year = (1985,)
cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchall())

connection.commit()
connection.close()