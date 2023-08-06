import logging
from random import choice
from string import ascii_lowercase
from typing import Any

import docker
from docker.models.containers import Container, ExecResult

from app.exceptions.container_not_started import ContainerNotStartedError


class DockerContainer:
    def __init__(
        self,
        client=docker.from_env(),
        logger=logging.getLogger(__name__),
    ) -> None:
        self._logger = logger
        self._client = client

    def run(self, image: str, environment: dict[str, str]) -> None:
        self._logger.debug(f"Running container from image: {image}")

        self._container: Container = self._client.containers.run(
            image,
            name=f"dbut-{self._generate_suffix()}",
            detach=True,
            auto_remove=True,
            environment=environment,
        )

    def reload(self) -> None:
        self._check_container()

        self._container.reload()

    def get_ip(self) -> str:
        self._check_container()

        self.reload()

        return self._container.attrs["NetworkSettings"]["IPAddress"]

    def exec_run(self, cmd: Any) -> ExecResult:
        return self._container.exec_run(cmd)

    def cleanup(self) -> None:
        try:
            self._check_container()
        except ContainerNotStartedError:
            pass
        except Exception as e:
            raise e
        else:
            self._container.stop()

    def _check_container(self) -> None:
        if not self._container:
            raise ContainerNotStartedError()

    def _generate_suffix(self) -> str:
        return "".join(choice(ascii_lowercase) for _ in range(8))
