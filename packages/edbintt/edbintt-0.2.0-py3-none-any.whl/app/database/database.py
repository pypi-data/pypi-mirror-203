from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine
from sqlalchemy.orm import Session

from app.models.database_configuration import DatabaseConfiguration


class Database:
    def __init__(self, database_configuration: DatabaseConfiguration) -> None:
        self._engine = self._create_engine(database_configuration)

    @property
    def engine(self) -> Engine:
        return self._engine

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        with Session(bind=self._engine) as session, session.begin():
            yield session

    def _create_engine(self, database_configuration: DatabaseConfiguration) -> Engine:
        return create_engine(
            URL.create(
                drivername=f"{database_configuration.engine}+psycopg2",
                username=f"{database_configuration.username}",
                password=f"{database_configuration.password}",
                host=f"{database_configuration.host}",
                port=int(database_configuration.port),
                database=f"{database_configuration.database}",
            ),
        )
