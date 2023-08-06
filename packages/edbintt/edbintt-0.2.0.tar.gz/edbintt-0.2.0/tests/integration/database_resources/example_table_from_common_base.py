from sqlalchemy import Column, Integer, String

from tests.integration.database_resources.base import Base


class ExampleTableFromCommonBase(Base):
    __tablename__ = "example_table_common_base"

    id = Column(Integer, primary_key=True, auto_increment=True)
    column_1 = Column(Integer)
    column_2 = Column(String(64))
