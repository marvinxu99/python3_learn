from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config


db_string = config("DB_PG_SQLALCHEMY")   # from .env
engine = create_engine(db_string)
Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Sales(Base):
    __table__ = Base.metadata.tables['sales']

    def __repr__(self) -> str:
        return (f"<Sale(order_num={self.order_num}, order_type={self.order_type}, "
            f"cust_name={self.cust_name}, prod_name={self.prod_name}, "
            f"quantity={self.quantity}, order_total={self.order_total}>") 


def load_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = load_session()

    # Read
    smallest_sales = session.query(Sales).order_by(Sales.order_total).limit(10)
    print(smallest_sales[0].cust_name, )
    print(smallest_sales[0])

    # Delete
    returned_sale = session.query(Sales).filter(Sales.order_num==1105910).first()
    if returned_sale:
        session.delete(returned_sale)
        session.commit()

    # Insert
    recent_sale = Sales(
            order_num = 1105910, 
            order_type = 'Retail', 
            cust_name = 'Syman Mapstone',
            prod_number = 'EB521', 
            prod_name = 'Understanding AI', 
            quantity = 3, 
            price = 19.5, 
            discount = 0, 
            order_total = 58.5
        )
    session.add(recent_sale)
    session.commit()

    # Update
    recent_sale.quantity = 2
    recent_sale.order_total = 39
    session.commit()
    updated_sale = session.query(Sales).filter(Sales.order_num==1105910).first()
    print(updated_sale)
