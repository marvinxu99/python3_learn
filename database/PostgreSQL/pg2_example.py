import psycopg2
from decouple import config


def main():
    conn_string = config("CONN_STRING2")  # from .env file
    # print(conn_string)    
    conn = psycopg2.connect(conn_string)

    # Open a cursor
    cursor = conn.cursor()


    # create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales 
        (order_num INT PRIMARY KEY,
          order_type TEXT,
          cust_name TEXT,
          prod_number BIGINT,
          prod_name TEXT,
          quantity INT,
          price REAL,
          discount REAL,
          order_total real
        ); ''')


    cursor.execute('''DROP TABLE IF EXISTS winter_test;''')
    cursor.execute('''CREATE TABLE winter_test 
          (winter_id INT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT
          ); ''')

    # Insert one row
    cursor.execute("""INSERT INTO winter_test(winter_id, first_name, last_name)
                             VALUES(%s, %s, %s);""", (1, 'winter', 'xu'))

    users_to_insert = ([
      (2, 'Wesley', 'Xu',),
      (3, 'Winter', 'Xu',),
      (4, 'Turbo', 'Xu',)
    ])
    cursor.executemany("""INSERT INTO winter_test(winter_id, first_name, last_name)
                             VALUES(%s, %s, %s);""", users_to_insert)

    conn.commit()

    # Select and retrieve results
    #cursor.execute("SELECT winter_id, first_name, TO_CHAR(date_joined, 'dd/mm/yyyy') FROM accounts_user")
    cursor.execute("SELECT winter_id, first_name, last_name FROM winter_test")
    records = cursor.fetchall()
    print(records)


    # Returns the current date of the database server
    # cursor.execute("SELECT NOW()::date")
    cursor.execute("SELECT TO_CHAR(NOW() :: DATE, 'dd/mm/yyyy hh:mm')")
    records = cursor.fetchall()
    print(records)

    # Close the cursor and the connection
    cursor.close()
    conn.close()


if __name__ == '__main__':  
  main()

