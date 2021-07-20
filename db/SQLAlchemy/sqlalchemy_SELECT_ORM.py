"""Selecting Rows with Core or ORM
https://docs.sqlalchemy.org/en/14/tutorial/data_select.html

For both Core and ORM, the select() function generates a Select construct 
which is used for all SELECT queries. Passed to methods like 
Connection.execute() in Core and Session.execute() in ORM, a SELECT statement 
is emitted in the current transaction and the result rows available via 
the returned Result object.
"""

from sqlalchemy import create_engine
from sqlalchemy import insert, select, bindparam
from sqlalchemy import MetaData, Table, Column, Integer, String, text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship


# Establish connectivity - the Engine
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

Base = declarative_base()

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

""" Insert Rows with Core for testing"""
# INSERT usually generates the “values” clause automatically
with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {'name': 'spongebob', 'fullname': "Spongebob Squarepants"},
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"},
        ]
    )
    conn.commit()

# Below is some slightly deeper alchemy just so that we can add related rows 
# without fetching the primary key identifiers from the user_table operation 
# into the application. Most Alchemists will simply use the ORM which takes 
# care of things like this for us.
scalar_subquery = (
    select(user_table.c.id)
    .where(user_table.c.name==bindparam('username'))
    .scalar_subquery()
)

with engine.connect() as conn:
    result = conn.execute(
        insert(address_table).values(user_id=scalar_subquery),
        [
            {"username": 'spongebob', "email_address": "spongebob@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@sqlalchemy.org"},
            {"username": 'sandy', "email_address": "sandy@squirrelpower.org"},
        ]
    )
    conn.commit()
    # result = conn.execute(
    #         select(
    #                 user_table.c.id, 
    #                 user_table.c.fullname, 
    #                 address_table.c.email_address
    #             )
    #         .where(user_table.c.id==address_table.c.user_id)
    #     )
    # print(result.all())


#########################################
""" ORM examples """

class User(Base):
    __table__ = user_table

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __table__ = address_table

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
         return f"Address({self.email_address!r})"


""" INSERT...FROM SELECT """
print("----INSERT...FROM SELECT ---")
select_stmt = select(User.id, User.name + "@aol.com")
insert_stmt = insert(Address).from_select(
    ["user_id", "email_address"], select_stmt
)
# print(insert_stmt)
with Session(engine) as session:
    result = session.execute(insert_stmt)
    session.commit()
    result = session.execute(select(Address))
    for r in result:
        print(r)


# ORM select()
print("---- select ORM ------")
stmt = select(User).where(User.name == "spongebob")
stmt2 = select(User.name, User.fullname).where(User.name == "spongebob")
# print(stmt)
with Session(engine) as session:
    for row in session.execute(stmt):
        # print(type(row))
        print(row)

    for row in session.execute(stmt2):
        # print(type(row))
        print(row)

    result = session.execute(
        select(User.name, Address).where(User.id==Address.user_id)
        .order_by(Address.id)
    )
    for row in result:
        print(row)
'''
(User(id=1, name='spongebob', fullname='Spongebob Squarepants'),)
('spongebob', 'Spongebob Squarepants')
'''

# Selecting from Labeled SQL Expressions
print("---Selecting from Labeled SQL Expressions---")
stmt = (
    select(
        ("Username: " + User.name).label('username'),
        User.fullname,
    ).order_by(User.name)
)
with Session(engine) as session:
    results = session.execute(stmt)
    # print(results.first())
    for row in results:
        # print(f"{row.username}")
        print(row.username, ', ', row.fullname)

# Selecting with Textual Column Expressions
print("--- Selecting with Textual Column Expressions ---")
stmt = (
    select(
        text("'some phrase'"), User.name, User.fullname
    ).order_by(User.name)
)
with Session(engine) as session:
    print(session.execute(stmt).all())

# In this common case we can get more functionality out of our textual 
# fragment using the literal_column() construct instead. This object is 
# similar to text() except that instead of representing arbitrary SQL of 
# any form, it explicitly represents a single “column” and can then be 
# labeled and referred towards in subqueries and other expressions
from sqlalchemy import literal_column
stmt = (
    select(
        literal_column("'some phrase'").label("p"), User.name
    ).order_by(User.name)
)
with Session(engine) as session:
    for row in session.execute(stmt):
        print(f"{row.p}, {row.name}")


# The WHERE clause
# (1) To produce expressions joined by AND, where() method maybe invoked any number of times:
print(
    select(Address.email_address).
    where(User.name == 'squidward').
    where(Address.user_id == User.id)
)
'''
SELECT address.email_address 
FROM address, user_account
WHERE user_account.name = :name_1 AND address.user_id = user_account.id
'''
#(2) A single call to Select.where() also accepts multiple expressions with the same effect:
print(
    select(Address.email_address).
    where(
        User.name == 'squidward',
        Address.user_id == User.id
    )
)
'''
SELECT address.email_address
FROM address, user_account
WHERE user_account.name = :name_1 AND address.user_id = user_account.id 
'''
# (3) “AND” and “OR” conjunctions are both available directly using the and_() 
# and or_() functions, illustrated below in terms of ORM entities:
from sqlalchemy import and_, or_
print(
    select(Address.email_address)
    .where(
        and_(
            or_(
                User.name == 'squidward', 
                User.name == 'sandy'
            ),
            Address.user_id == User.id
        )
    )
)
"""
SELECT address.email_address
FROM address, user_account
WHERE (user_account.name = :name_1 OR user_account.name = :name_2) AND address.user_id = user_account.id
"""
#(4) select().filter_by()
print(
    select(User).filter_by(name='spongebob', fullname='Spongebob Squarepants')
)
"""
SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
WHERE user_account.name = :name_1 AND user_account.fullname = :fullname_1 
"""

# Explicit FROM clauses and JOINs
print("--- Explicit FROM clauses and JOINs ---")
# (1) select().join_from()
print(
    select(User.name, Address.email_address)
    .join_from(User, Address)
) 
"""
SELECT user_account.name, address.email_address
FROM user_account JOIN address ON user_account.id = address.user_id 
"""

# (2) Select.join() method, which indicates only the right side of the JOIN, 
# the left hand-side is inferred:
print(
    select(User.name, Address.email_address).
    join(Address)
)
"""
SELECT user_account.name, address.email_address
FROM user_account JOIN address ON user_account.id = address.user_id  
"""
# (3) Select.from() method - used if the columns clause does not
print(
    select(User.name, Address.email_address).
    select_from(User).join(Address)
)

# Select.from() method is used if the columns clause does not have enough info 
# to provide for a FROM clause.
from sqlalchemy import func
print (
    select(func.count('*')).select_from(User)
)
"""
SELECT count(:count_2) AS count_1
FROM user_account
"""

# Setting on the ON Clause
# Both Select.join() and Select.join_from() accept an additional argument 
# for the ON clause, which is stated using the same SQL Expression mechanics 
# as we saw about in The WHERE clause
print("--- Setting on the ON Clause ---")
print(
    select(Address.email_address)
    .select_from(User)
    .join(Address, User.id == Address.user_id)
)
"""
SELECT address.email_address
FROM user_account JOIN address ON user_account.id = address.user_id 
"""

# OUTER and FULL join
# Both the Select.join() and Select.join_from() methods accept keyword 
# arguments Select.join.isouter and Select.join.full which will render 
# LEFT OUTER JOIN and FULL OUTER JOIN, respectively:
print("--- OUTER and FULL join ---")
# stmt1 = select(User).join(Address, isouter=True)
stmt1 = select(User.name, Address.email_address).outerjoin(Address)
print(stmt1)
"""
SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account LEFT OUTER JOIN address ON user_account.id = address.user
"""
stmt2 = select(User.name, Address.email_address).join(Address, full=True)
print(stmt2)
"""
SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account FULL OUTER JOIN address ON user_account.id = address.user_id
"""
with Session(engine) as session:
    # print(session.execute(select(User)).all())
    # print(session.execute(select(Address)).all())
    print(session.execute(stmt1).all())
    # print(session.execute(stmt2).all())   # FULL and RIGHT Outer join not suppored in sqllite3


# ORDER BY, GROUP BY, HAVING
print(" --- ORDER BY, GROUP BY, HAVING ---")
print(select(User).order_by(User.name.asc()))
print(select(User).order_by(User.fullname.desc()))

# Aggregate functions with GROUP BY / HAVING
# SQLAlchemy provides for SQL functions in an open-ended 
# way using a namespace known as func
print("--- Aggregate functions with GROUP BY / HAVING ---")
from sqlalchemy import func
# count_fn = func.count(user_table.c.id)
# print(count_fn)
with engine.connect() as conn:
    result = conn.execute(
        select(User.name, func.count(Address.id).label("count")).
        join(Address).
        group_by(User.name).
        having(func.count(Address.id) > 1)
    )
    print(result.all())
"""
count(user_account.id)
[('sandy', 3), ('spongebob', 2)]
"""
# rdering or Grouping by a Label
from sqlalchemy import func, desc
stmt = select(Address.user_id, User.name,
        func.count(Address.id).label('num_addresses')). \
        join(Address). \
        group_by("user_id").order_by("user_id", desc("num_addresses"))
print(stmt)
with Session(engine) as session:
    result = session.execute(stmt)
    print(result.all())

# Using Alias
print("--- Using Alias ---")
from sqlalchemy.orm import aliased
address_alias_1 = aliased(Address)
address_alias_2 = aliased(Address)
print(
    select(User).
    join_from(User, address_alias_1).
    where(address_alias_1.email_address == 'patrick@aol.com').
    join_from(User, address_alias_2).
    where(address_alias_2.email_address == 'patrick@gmail.com')
)

# Subqueries and CTEs
print("--- Subqueries and CTEs ---")
subq = select(Address).where(~Address.email_address.like('%@aol.com')).subquery()
address_subq = aliased(Address, subq)
stmt = select(User, address_subq).join_from(User, address_subq).order_by(User.id, address_subq.id)
with Session(engine) as session:
    for user, address in session.execute(stmt):
        print(f"{user} {address}")
