"""SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/data.html
To create, select and manipulate data within a relational database
"""

from sqlalchemy import create_engine
from sqlalchemy import insert
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


# Manipulate databases...


