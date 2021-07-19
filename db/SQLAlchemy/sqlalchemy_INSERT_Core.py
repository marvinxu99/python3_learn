"""SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/data.html
To create, select and manipulate data within a relational database
"""

from sqlalchemy import create_engine
from sqlalchemy import insert, select, bindparam
from sqlalchemy import MetaData, Table, Column, Integer, String
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

""" INSERT...RETURNING"""
print('----- INSERT...RETURNING------')
insert_stmt = insert(address_table).returning(address_table.c.id, address_table.c.email_address)
print(insert_stmt)    # it is not supported by the sqlite3 dialect statememt compiler
# with engine.connect() as conn:
#     result = conn.execute(
#         insert_stmt,
#         [
#             {"user_id": 1, "email_address": "spongebob@sqlalchemy.org"},
#             {"user_id": 2, "email_address": "sandy@sqlalchemy.org"},
#         ]
#     )
#     conn.commit()

# RETURNING can be used in SELECT statement as well
# select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
# insert_stmt = insert(address_table).from_select(
#     ["user_id", "email_address"], select_stmt
# ).returning(address_table.c.id, address_table.c.email_address)
# print(insert_stmt)
# with engine.connect() as conn:
#     result = conn.execute(insert_stmt)
#     conn.commit()
#     result = conn.execute(select(address_table))
#     for r in result:
#         print(r)


