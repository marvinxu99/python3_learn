""" Database manipulation using SQLAlchemy ORM
"""

from sqlalchemy import create_engine
from sqlalchemy import insert, select, bindparam
from sqlalchemy import MetaData, Table, Column, Integer, String, text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship
from decouple import config         # pip install python-decouple


# Establish connectivity - the Engine
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
db_string = config("DB_PG_WINN_DEV_6")   # from .env
engine = create_engine(db_string, echo=False, future=True)

Base = declarative_base(engine)
Base.metadata.reflect(engine)

cv_table = Table("core_code_value", Base.metadata, autoload_with=engine)
print(cv_table)

class CodeValue(Base):
    __table__ = Base.metadata.tables['core_code_value']

    def __repr__(self) -> str:
        return (f"<CodeValue(code_set_id={self.code_set_id}, display={self.display})")


print("--- Accessing tables ---")
for t in Base.metadata.sorted_tables:
    print(t.name)

print("--- list all the table columns ---")
# print(CodeValue.__table__.c)
print(CodeValue.__table__.columns)


# access the column "employee_id":
print(CodeValue.columns.code_value)

# or just
employees.c.employee_id

# via string
employees.c['employee_id']

# iterate through all columns
for c in employees.c:
    print(c)

# get the table's primary key columns
for primary_key in employees.primary_key:
    print(primary_key)

# get the table's foreign key objects:
for fkey in employees.foreign_keys:
    print(fkey)