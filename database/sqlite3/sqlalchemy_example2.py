import sqlalchemy as db
from sqlalchemy.sql.schema import Column


engine = db.create_engine('sqlite:///users-sqlalchemy.db')
connection = engine.connect()
metadata = db.MetaData()
users = db.Table('users', metadata, 
        db.Column('user_id', db.Integer, primary_key=True),
        db.Column('first_name', db.Text),
        db.Column('last_name', db.Text),
        db.Column('email', db.Text)
    )
metadata.create_all(engine)

user_list = [
    {'first_name': 'Quentin', 'last_name': 'Tarantino', 'email': 'qt@gamil.com'},
    {'first_name': 'Steven', 'last_name': 'Spielberg', 'email': 'steven@gamil.com'},
    {'first_name': 'West', 'last_name': 'Anderson', 'email': 'west@gail.com'}
]
insert_query = users.insert().values(user_list)
connection.execute(insert_query)

query = db.select([users])
result_set = connection.execute(query).fetchall()
print(result_set)

# Only display Email
query = db.select([users.columns.email])
result_set = connection.execute(query).fetchall()
print(result_set)

# display Email
query = db.select([users.columns.email]).where(users.columns.first_name=='Steven')
result_set = connection.execute(query).fetchone()
print(result_set[0])
