from pydantic import BaseModel


class DatabaseConfiguration(BaseModel):
    engine: str
    username: str
    password: str
    host: str
    port: int
    database: str
