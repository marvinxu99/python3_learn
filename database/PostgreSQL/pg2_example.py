import psycopg2
from decouple import config


def main():
    conn_string = config("CONN_STRING2")

    print(conn_string)    
    conn = psycopg2.connect(conn_string)

    # Open a cursor
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO winter_test (winter_id, first_name, last_name)
                             VALUES(%s, %s, %s)""", [3, "winter", 'Xu'])

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

