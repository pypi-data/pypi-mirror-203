from typing import Generator

import pytest
from sqlalchemy.orm import Session

from app.database.database import Database
from app.sqlalchemy_package.postgres import Postgres
from tests.integration.database_resources.example_table_from_own_base import (
    ExampleTableFromOwnBase,
)


class TestPostgresDataResetTableWithNoInitData:
    @pytest.fixture(scope="class")
    def postgres(self) -> Generator[Postgres, None, None]:
        with Postgres(version="15.2", tables=[ExampleTableFromOwnBase]) as postgres:
            yield postgres

    @pytest.fixture(scope="class")
    def database(self, postgres: Postgres) -> Database:
        return Database(database_configuration=postgres._database_configuration)

    @pytest.fixture(autouse=True)
    def reset_postgres(self, postgres: Postgres) -> None:
        postgres.reset()

    def test_add_first_batch(self, database: Database) -> None:
        with database.session() as session:
            self._add_batch(session)

        with database.session() as session:
            self._assert_data(session)

    def test_add_second_batch(self, database: Database) -> None:
        with database.session() as session:
            self._add_batch(session)

        with database.session() as session:
            self._assert_data(session)

    def test_add_third_batch(self, database: Database) -> None:
        with database.session() as session:
            self._add_batch(session)

        with database.session() as session:
            self._assert_data(session)

    def _add_batch(self, session: Session) -> None:
        session.add_all(
            [
                ExampleTableFromOwnBase(column_1=1, column_2="one"),
                ExampleTableFromOwnBase(column_1=2, column_2="two"),
                ExampleTableFromOwnBase(column_1=3, column_2="three"),
            ]
        )

    def _assert_data(self, session: Session):
        rows = session.query(ExampleTableFromOwnBase).order_by(
            ExampleTableFromOwnBase.id
        )

        expected_row_values = [
            {"id": 1, "column_1": 1, "column_2": "one"},
            {"id": 2, "column_1": 2, "column_2": "two"},
            {"id": 3, "column_1": 3, "column_2": "three"},
        ]

        number_of_rows = 0
        for index, row in enumerate(rows):
            number_of_rows += 1

            assert row.id == expected_row_values[index]["id"]
            assert row.column_1 == expected_row_values[index]["column_1"]
            assert row.column_2 == expected_row_values[index]["column_2"]

        assert number_of_rows == len(expected_row_values)
