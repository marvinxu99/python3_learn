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
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import text
from sqlalchemy import ForeignKey


# Establish connectivity - the Engine
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

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

""" Insert Rows with Core"""
stmt = insert(user_table).values(name='spongebob', fullname="Spongebob Squarepants")
# print(stmt)
# compiled = stmt.compile()
# print(compiled.params)
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
    print(result.inserted_primary_key)


# INSERT usually generates the “values” clause automatically
with engine.connect() as conn:
    result = conn.execute(
        insert(user_table),
        [
            {"name": "sandy", "fullname": "Sandy Cheeks"},
            {"name": "patrick", "fullname": "Patrick Star"}
        ]
    )
    conn.commit()
    result = conn.execute(select(user_table))
    print(result.all())

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
    result = conn.execute(
            select(
                    user_table.c.id, 
                    user_table.c.fullname, 
                    address_table.c.email_address
                )
            .where(user_table.c.id==address_table.c.user_id)
        )
    print(result.all())

""" INSERT...FROM SELECT """
print("----INSERT...FROM SELECT ---")
select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
insert_stmt = insert(address_table).from_select(
    ["user_id", "email_address"], select_stmt
)
# print(insert_stmt)
with engine.connect() as conn:
    result = conn.execute(insert_stmt)
    conn.commit()
    result = conn.execute(select(address_table))
    for r in result:
        print(r)

#########################################
""" 
Selecting Rows with Core
"""
print("----Selecting Rows with Core ----")
stmt = select(user_table).where(user_table.c.name=='spongebob')
stmt2 = select(user_table.c.name, user_table.c.fullname).where(user_table.c.name=='spongebob')
# print(stmt)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

    for row in conn.execute(stmt2):
        # print(type(row))
        print(row)
'''
(1, 'spongebob', 'Spongebob Squarepants')
('spongebob', 'Spongebob Squarepants')
'''

# Selecting from Labeled SQL Expressions
print("---Selecting from Labeled SQL Expressions---")
stmt = (
    select(
        ("Username: " + user_table.c.name).label('username'),
        user_table.c.fullname,
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.username} {row.fullname}")

# Selecting with Textual Column Expressions
print("--- Selecting with Textual Column Expressions ---")
stmt = (
    select(
        text("'some phrase'"), user_table.c.name
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    print(conn.execute(stmt).all())

# In this common case we can get more functionality out of our textual 
# fragment using the literal_column() construct instead. This object is 
# similar to text() except that instead of representing arbitrary SQL of 
# any form, it explicitly represents a single “column” and can then be 
# labeled and referred towards in subqueries and other expressions
from sqlalchemy import literal_column
stmt = (
    select(
        literal_column("'some phrase'").label("p"), user_table.c.name
    ).order_by(user_table.c.name)
)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(f"{row.p}, {row.name}")