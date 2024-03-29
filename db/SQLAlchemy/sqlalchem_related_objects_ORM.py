"""SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/data.html
To create, select and manipulate data within a relational database
"""

from sqlalchemy import create_engine
from sqlalchemy import select, update, delete, insert, bindparam
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session, aliased, selectinload
from sqlalchemy.orm import declarative_base, relationship


# Establish connectivity - the Engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

Base = declarative_base()

# Defining Table Metadata with the ORM
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

Base.metadata.create_all(engine)

# Manipulate databases...
print("--- Instances of Classes represent Rows ---")
squidward = User(name="squidward", fullname='Squidward Tentacles')
krabs = User(name='ehkrabs', fullname='Eugene H. Krabs')
sandy = User(name="sandy", fullname="Sandy Cheeks")
patrick = User(name="patrick", fullname="Patrick Starr")
spongebob = User(name='spongebob', fullname='spongebob squarpants')
# print(id(krabs))

with Session(engine) as session:
    session.add(spongebob)
    session.add(squidward)
    session.add(krabs)
    session.add(sandy)
    session.add(patrick)

    # print(session.new)  # to see a collection on the session
    #session.flush()

    print(session.execute(select(User)).all())
    # print(squidward)
    # print(session.get(User, 1))
    session.commit()

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


print("--- working with related objects ---")
with Session(engine) as session:
    sandy = session.execute(select(User).filter_by(name="sandy")).scalar_one()
    print(sandy.addresses)   
    print(sandy.addresses[0].email_address)   
    sandy.addresses[0].email_address = "newemail@gmail.com"
    print(session.execute(
        select(User.name, Address.email_address).
        where(User.id == Address.user_id and User.name == 'sandy'))
    )
    session.commit()

print("--- Persisting and Loading Relationships ---")
with Session(engine) as session:
    u1 = User(name='pkrabs', fullname='Pearl Krabs')
    print(u1.addresses)

    a1 = Address(email_address="pearl.krabs@gmail.com")
    u1.addresses.append(a1)
    print(u1.addresses)
    print(a1.user)

    a2 = Address(email_address="pearl@aol.com", user=u1)
    # a2 = Address(email_address="pearl@aol.com")
    # a2.user = u1
    print(u1.addresses)

    print("--- adding u1 will auto add a1, a2 ---")
    session.add(u1)  # will also atuo add a1 & a2
    session.flush()

    print(session.execute(
        select(User.name, Address.email_address).
        where(User.id == Address.user_id)).all()
    )
    session.commit()

    print('-- loading relationship ---')
    print(u1.id)
    print(u1.addresses)

print("--- Using Relationships to Join ---")
with Session(engine) as session:
    result = session.execute(
        select(User.name, Address.email_address).
        select_from(User).
        where(User.name == 'sandy').
        join(User.addresses)
    )
    print(result.all())

print("--- Joining between Aliased targets ---")
address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)
print(
      select(User).
       join(User.addresses.of_type(address_alias_1)).
       where(address_alias_1.email_address == 'patrick@aol.com').
       join(User.addresses.of_type(address_alias_2)).
       where(address_alias_2.email_address == 'patrick@gmail.com')
   )

user_alias_1 = aliased(User)
print(
    select(user_alias_1.name).
    join(user_alias_1.addresses)
)

print("--- Augmenting the ON Criteria ---")
stmt = (
    select(User.fullname).
    join(User.addresses.and_(Address.email_address == "pearl.krabs@gmail.com"))
)
with Session(engine) as session:
    print(session.execute(stmt).all())


print("--- Loader Strategy ---")
with Session(engine) as session:
    for user_obj in session.execute(
        select(User).options(selectinload(User.addresses))
        # .where(User.addresses != None)
        ).scalars():
            print(user_obj.name, user_obj.addresses)  # access addresses collection already loaded

print("--- selectinload() ---")
from sqlalchemy.orm import selectinload
stmt = (
    select(User).options(selectinload(User.addresses)).order_by(User.id)
)
with Session(engine) as session:
    for row in session.execute(stmt):
        print(f"{row.User.name}  ({', '.join(a.email_address for a in row.User.addresses)})")

print("--- joinedload ---")
from sqlalchemy.orm import joinedload
stmt = (
    select(Address).options(joinedload(Address.user, innerjoin=True)).order_by(Address.id)
)
with Session(engine) as session:
    for row in session.execute(stmt):
        print(f"{row.Address.email_address} {row.Address.user.name}")

print("--- Explicit Join + Eager load ---")

#Augmenting Loader Strategy Paths
