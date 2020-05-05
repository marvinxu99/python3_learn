import sqlite3
from sqlite3 import Error

# conn = sqlite3.connect('mydatabase.db')
# cursorObj = conn.cursor()

def sql_connection():
    try:
        # conn = sqlite3.connect(':memory:')   # in memory database
        # print("Connection is established: Database is created in memory")
        conn = sqlite3.connect('mydatabase.db')
        return conn
    except Error:
        print(Error)


def sql_create_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute('''CREATE TABLE employees(id integer PRIMARY KEY, name text, 
            salary real, department text, position text, hireDate text)''')
    conn.commit()
    cursorObj.close()

def sql_insert(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO employees VALUES(2, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    conn.commit()
    cursorObj.close()

def sql_insert2(con, entities):
    cursorObj = con.cursor()   
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    con.commit()
    cursorObj.close()

def sql_update(conn):
    cursorObj = conn.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    conn.commit()
    cursorObj.close()

def sql_update(conn):
    cursorObj = conn.cursor()
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    conn.commit()
    cursorObj.close()

def sql_fetch(conn):
    cursorObj = conn.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)

    cursorObj.close()


conn = sql_connection()

# sql_create_table(conn)

# sql_insert(conn)

# entities = (3, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
# sql_insert2(conn, entities)

# sql_update(conn)

sql_fetch(conn)

conn.close()
