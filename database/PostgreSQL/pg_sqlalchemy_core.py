from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
from decouple import config


db_string = config("DB_PG_SQLALCHEMY")   # from .env
engine = create_engine(db_string)
# print(engine)

with engine.connect() as connection:
    meta = MetaData(engine)
    sales_table = Table('sales', meta, autoload=True, autoload_with=engine)

    # Delete
    delete_statement = sales_table.delete().where(sales_table.c.order_num==1105910)
    connection.execute(delete_statement)
    
    # Create a row
    insert_statement = sales_table.insert().values(
        order_num = 1105910, 
        order_type = 'Retail', 
        cust_name = 'Syman Mapstone',
        prod_number = 'EB521', 
        prod_name = 'Understanding AI', 
        quantity = 3, 
        price = 19.5, 
        discount = 0, 
        order_total = 58.5)
    connection.execute(insert_statement)

    # read
    # select_statement = sales_table.select().limit(10)
    select_statement = sales_table.select().where(sales_table.c.order_num==1105910)
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = sales_table.update().where(sales_table.c.order_num==1105910).values(quantity=100)
    connection.execute(update_statement)
    select_statement = sales_table.select().where(sales_table.c.order_num==1105910)
    result_set = connection.execute(select_statement)
    for r in result_set:
        print(r)

