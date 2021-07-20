"""SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/data.html
To create, select and manipulate data within a relational database
"""

from sqlalchemy import create_engine
from sqlalchemy import insert, select, bindparam, update
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base, relationship
from decouple import config         # pip install python-decouple


# Establish connectivity - the Engine
# # engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)
# db_string = config("DB_PG_SQLALCHEMY")   # from .env
# engine = create_engine(db_string)

"""
Setting up MetaData with Table objects (SQLAlchemy Core)
"""
# MetaData object
metadata = MetaData()

"""
Defining Table Metadata with the SQLAlchemy ORM
"""
# mapper_registry = registry()
# print(mapper_registry.metadata)
# Base = mapper_registry.generate_base()
'''The steps of creating the registry and “declarative base” classes can be 
combined into one step using the historically familiar declarative_base() function:'''
Base = declarative_base()
print(Base)

class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# print(User.__table__)
# print(Address.__table__)

# emit CREATE statements if given ORM registry
# mapper_registry.metadata.create_all(engine)
# The identical MetaData object is also present on the
# declarative base
Base.metadata.create_all(engine)


""" Insert Rows with Core"""
print("--- Insert Rows with Core ---")
stmt = insert(User).values(name='spongebob', fullname="Spongebob Squarepants")
with Session(engine) as session:
    result = session.execute(stmt)
    session.commit()
    print(result.inserted_primary_key)


# INSERT usually generates the “values” clause automatically
with Session(engine) as session:
    result = session.execute(
        insert(User),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"}
        ]
    )
    session.commit()
    result = session.execute(select(User))
    print(result.all())

# Below is some slightly deeper alchemy just so that we can add related rows 
# without fetching the primary key identifiers from the user_table operation 
# into the application. Most Alchemists will simply use the ORM which takes 
# care of things like this for us.
print("--- Insert Rows with scalar subquery ---")
scalar_subquery = (
    select(User.id)
    .where(User.name==bindparam('username'))
    .scalar_subquery()
)
with Session(engine) as session:
    result = session.execute(
        insert(Address).values(user_id=scalar_subquery),
        [
            {"username": 'spongebob', "email_address": "spongebob@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@squirrelpower.org"},
        ]
    )
    session.commit()
    result = session.execute(
            select(
                    User.id, 
                    User.fullname, 
                    Address.email_address
                )
            .where(User.id == Address.user_id)
        )
    print(result.all()) 

# Update 
# The update() SQL Expression Construct
print("--- # Update SQL Expression ---")
stmt = (
    update(User).where(User.name == 'patrick').
    values(fullname='Patrick Swap')
)
with Session(engine) as session:
    result = session.execute(stmt)
    session.commit()
    result = session.execute(select(User))
    print(result.all())

# Update executemany():
print("--- # Update executemany(), bindparam ---")
stmt = (
    update(User).
    where(User.name == bindparam('oldname')).
    values(fullname=bindparam('newname'))
)
print(stmt)
with Session(engine) as session:
    session.execute(
        stmt,
        [
            {'oldname':'patrick', 'newname':'ed'},
            {'oldname':'spongebob', 'newname':'mary'},
            {'oldname':'jim', 'newname':'jake'},
        ]
    )
    session.commit()
    print(session.execute(select(User)).all())

# Correlated Updates
print("--- Correlated Updated ---")
scalar_subq = (
    select(Address.email_address).
    where(Address.user_id == User.id).
    order_by(Address.id).
    limit(1).
    scalar_subquery()
)
update_stmt = (
    update(User).
    # where(User.id==1).
    values(fullname=scalar_subq)
)
print(update_stmt)
with Session(engine) as session:
    session.execute(update_stmt)
    session.commit()
    result = session.execute(select(User))
    print(result.all())

# UPDATE..FROM
print("--- Update.. FROM ---")
"""
>>> update_stmt = (
...    update(user_table).
...    where(user_table.c.id == address_table.c.user_id).
...    where(address_table.c.email_address == 'patrick@aol.com').
...    values(fullname='Pat')
...  )
>>> print(update_stmt)
UPDATE user_account SET fullname=:fullname FROM address
WHERE user_account.id = address.user_id AND address.email_address = :email_address_1
"""