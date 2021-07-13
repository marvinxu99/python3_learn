import psycopg2
import sys

def main():
    conn_string = "host='localhost' port=5432 dbname='winn_users6' user='winter' password='winter'"
    conn = psycopg2.connect(conn_string)

    # Open a cursor
    cursor = conn.cursor()

    # cursor.execute("""INSERT INTO traffic (yearMonth, users, sessions)
    #                         VALUES(%s, %s, %s)""", [row[0], row[1], row[2]])

    # conn.commit()

    # Select and retrieve results
    cursor.execute("SELECT username, email, TO_CHAR(date_joined, 'dd/mm/yyyy') FROM accounts_user")
    records = cursor.fetchall()
    print(records)

    # eturns the current date of the database server
    # cursor.execute("SELECT NOW()::date")
    cursor.execute("SELECT TO_CHAR(NOW() :: DATE, 'dd/mm/yyyy hh:mm')")
    records = cursor.fetchall()
    print(records)

    # Close the cursor and the connection
    cursor.close()
    conn.close()


if __name__ == '__main__':  
  main()

