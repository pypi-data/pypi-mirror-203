from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ExampleTableFromOwnBase(Base):
    __tablename__ = "example_table_own_base"

    id = Column(Integer, primary_key=True, auto_increment=True)
    column_1 = Column(Integer)
    column_2 = Column(String(64))
