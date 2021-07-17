"""
SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/metadata.html
"""
# The central element of both SQLAlchemy Core and ORM is the 
# SQL Expression Language which allows for fluent, composable construction0
#  of SQL queries. The foundation for these queries are Python objects 
# that represent database concepts like tables and columns. 
# These objects are known collectively as database metadata.

# The most common foundational objects for database metadata in SQLAlchemy 
# are known as MetaData, Table, and Column. 

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base, relationship


# Establish connectivity - the Engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

"""
Setting up MetaData with Table objects (SQLAlchemy Core)
"""
# MetaData object
metadata = MetaData()

# user_account
user_table = Table(
        "user_account",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String(30)),
        Column('fullname', String)
    )
# print(repr(user_table.c.name))
# print(user_table.c.keys())
# print(user_table.primary_key)

# Primary Key & Foreign Key
# When using the ForeignKey object within a Column definition, we can omit 
# the datatype for that Column; it is automatically inferred from that 
# of the related column, in the above example the Integer datatype of 
# the user_account.id column
address_table = Table(
        "address",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('user_id', ForeignKey('user_account.id'), nullable=False),
        Column('email_address', String, nullable=False)
    )

# Create the database
metadata.create_all(engine)

# Manipulate databases...

# Drop the tables
metadata.drop_all(engine)


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

"""
Combining Core Table Declarations with ORM Declarative
(Hybrid table)

Make use of the Table objects we created directly in the section Setting up 
MetaData with Table objects in conjunction with declarative mapped classes 
from a declarative_base() generated base class.

This form is called hybrid table, and it consists of assigning to 
the .__table__ attribute directly, rather than having the declarative process 
generate it.
"""
# class User(Base):
#     __table__ = user_table

#      addresses = relationship("Address", back_populates="user")

#      def __repr__(self):
#         return f"User({self.name!r}, {self.fullname!r})"

# class Address(Base):
#     __table__ = address_table

#      user = relationship("User", back_populates="addresses")

#      def __repr__(self):
#          return f"Address({self.email_address!r})"

