import sqlalchemy as db

"""
Users table was created in sqlite3_example2.py
"""

engine = db.create_engine('sqlite:///users.db')
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('Users', metadata, autoload=True, autoload_with=engine)

query = db.select([users])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

# Only display Email
query = db.select([users.columns.Email])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

# display Email
query = db.select([users.columns.Email]).where(users.columns.First_Name=='Steven')
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set[0][0])

# Insert a new user
query = users.insert().values(User_Id=4, First_Name="Alfred", Last_Name="Hotchcock", Email="alfres@gmail.com")
connection.execute(query)
query = db.select([users])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)
