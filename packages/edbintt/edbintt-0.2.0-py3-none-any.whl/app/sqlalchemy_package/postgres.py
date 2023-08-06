import logging
from time import sleep
from typing import Any

from app.database.database import Database
from app.docker_container.docker_container import DockerContainer
from app.exceptions.db_init_took_too_long import DbInitTookTooLongError
from app.exceptions.postgres_init import PostgresInitError
from app.models.database_configuration import DatabaseConfiguration
from app.types.sqlalchemy.new_row import NewRow
from app.types.sqlalchemy.new_row_dict import NewRowDict


class Postgres:
    _password = "mysecretpassword"

    def __init__(
        self,
        version: str,
        container=DockerContainer(),
        base: Any | None = None,
        tables: list[Any] | None = None,
        data: dict[Any, list[NewRow]] | None = None,
        wait_for_db_init_seconds=10,
        logger=logging.getLogger(__name__),
    ) -> None:
        if not base and not tables:
            raise PostgresInitError(
                "at least one of 'base' or 'tables' needs to be defined"
            )

        self._logger = logger
        self._version = version
        self._container = container
        self._base = base
        self._tables = tables
        self._data = self._parse_data(data) if data else None
        self._wait_for_db_init_seconds = wait_for_db_init_seconds

    def __enter__(self) -> "Postgres":
        try:
            self._run()
            self._wait_for_db_init()
            self._set_database_configuration()
            self._create_db_connection()
            self._setup()
        except Exception as e:
            self.__exit__(
                None,
                None,
                None,
            )

            raise e

        return self

    def __exit__(self, exc_type: Any, exc_value: Any, exc_tb: Any) -> None:
        self._container.cleanup()

    def reset(self) -> None:
        if self._base:
            self._base.metadata.drop_all(bind=self._database.engine, checkfirst=True)

        if self._tables:
            for table in self._tables:
                table.__table__.drop(self._database.engine, checkfirst=True)

        self._setup()

    def _parse_data(self, data: dict[Any, list[NewRow]]) -> dict[Any, list[NewRowDict]]:
        return {
            table: self._parse_rows_to_dict_list(rows) for table, rows in data.items()
        }

    def _parse_rows_to_dict_list(self, rows: list[NewRow]) -> list[NewRowDict]:
        rows_asdict: list[NewRowDict] = []

        for row in rows:
            asdict = row.__dict__

            if "_sa_instance_state" in asdict:
                del asdict["_sa_instance_state"]

            rows_asdict.append(asdict)

        return rows_asdict

    def _run(self) -> None:
        self._container.run(
            image=f"postgres:{self._version}",
            environment={"POSTGRES_PASSWORD": self._password},
        )

    def _wait_for_db_init(self) -> None:
        for retry in range(self._wait_for_db_init_seconds):
            self._logger.debug(
                f"Waiting for db init to be finished.. (retry '{retry}')"
            )

            result = self._container.exec_run("pg_isready")

            if result.exit_code == 0:
                self._logger.debug("Db init finished!")

                return

            sleep(1)

        raise DbInitTookTooLongError()

    def _set_database_configuration(self) -> None:
        self._database_configuration = DatabaseConfiguration(
            engine="postgresql",
            username="postgres",
            password=self._password,
            host=self._container.get_ip(),
            port=5432,
            database="postgres",
        )

    def _create_db_connection(self) -> None:
        self._database = Database(database_configuration=self._database_configuration)

    def _setup(self) -> None:
        if self._base:
            with self._database.session() as session:
                self._base.metadata.create_all(
                    bind=session.connection(), checkfirst=True
                )

        if self._tables:
            for table in self._tables:
                table.__table__.create(self._database.engine, checkfirst=True)

        if self._data:
            with self._database.session() as session:
                for table, rows in self._data.items():
                    session.add_all([table(**row) for row in rows])
