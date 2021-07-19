"""
SQLAlchemy TUtorial:
https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
"""


from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import Session


# Establish connectivity - the Engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Getting a connection - "commit as you go" style
with engine.connect() as conn:
    # result = conn.execute(text("select 'Hello World.'"))
    # print(result.all())
    conn.execute(text("CREATE TABLE IF NOT EXISTS some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()
    result = conn.execute(text("select * from some_table"))
    print(result.all())

# "Begin Once" style:
# “Begin once” style is often preferred as it is more succinct and indicates 
# the intention of the entire block up front
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [
            {"x": 6, "y": 8}, 
            {"x": 9, "y": 9},
            {"x": 9, "y": 8}, 
            {"x": 13, "y": 9},        
        ]
    )

# Fetching rows
print("----Fetching rows----")
with engine.connect() as conn:
    result = conn.execute(text("select x, y from some_table"))
    # for row in result:
    #     print(f"x: {row.x}  y: {row.y}")
    for x, y in result:
        print(f"x: {x}  y: {y}")

    # WHERE
    result = conn.execute(
        text("select x, y from some_table WHERE y >= :y"),
        {"y": 8}
    )
    for x, y in result:
        print(f"x: {x}  y: {y}")


# Bundling parameters with a statement
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with engine.connect() as conn:
    result = conn.execute(stmt)
    for x, y in result:
        print(f"x: {x}  y: {y}")


'''
Executing with an ORM Session
'''
print("---- session execute ----")
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)
with Session(engine) as session:
    result = session.execute(stmt)
    for x, y in result:
        print(f"x: {x}  y: {y}")

# UpDATE
with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y":11}, {"x": 13, "y": 15}]
    )
    session.commit()

    result = session.execute(stmt)
    for x, y in result:
        print(f"x: {x}  y: {y}")
