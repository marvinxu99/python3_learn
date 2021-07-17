import psycopg2
from decouple import config

def insert_sale(conn, order_num, order_type, cust_name, prod_number, 
        prod_name, quantity, price, discount):
    
    order_total = price * quantity
    if discount != 0:
        order_total = order_total * (1 - discount)
    
    sale_data = (order_num, order_type, cust_name, prod_number, 
            prod_name, quantity, price, discount, order_total)
     
    cur = conn.cursor()
    sql = '''INSERT INTO sales(order_num, order_type, 
            cust_name, prod_number, prod_name, quantity, price, 
            discount, order_total) VALUES(%s,%s,%s,%s,%s, %s,%s, %s,%s)'''
    cur.execute(sql, sale_data)
    conn.commit()

    # Query result
    cur.execute('''SELECT order_num, cust_name, order_total 
                FROM sales WHERE order_num=%s;''', (order_num,))
    records = cur.fetchall()
    print(records)


def main():
    conn_string = config("CONN_STRING2")  # from .env file
    # print(conn_string)    
    conn = psycopg2.connect(conn_string)

    # Open a cursor
    cursor = conn.cursor()


    # cursor.execute('''DROP TABLE IF EXISTS sales;''')

    # create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales 
        (order_num INT PRIMARY KEY,
          order_type TEXT,
          cust_name TEXT,
          prod_number TEXT,
          prod_name TEXT,
          quantity INT,
          price REAL,
          discount REAL,
          order_total real
        ); ''')


    # Query table
    cursor.execute("SELECT * FROM sales LIMIT 10;")
    records = cursor.fetchall()
    # print(records)

    # Insert one row
    # cursor.execute("""INSERT INTO sales(order_num, order_type, 
    #         cust_name, prod_number, prod_name, quantity, price, 
    #         discount, order_total) VALUES(1105910, 'Retail', 'Syman Mapstone',
    #         'EB521', 'Understanding AI', 3, 19.5, 0, 58.5);""")

    # conn.commit()

    # Query table
    cursor.execute("SELECT * FROM sales WHERE order_num=1105910;")
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

