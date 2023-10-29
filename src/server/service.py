import fastapi
import peewee
from src.server.database.pydantic_models import BaseModelModify


class RouterManager:
    def __init__(self, database_model: peewee.Model, pydantic_model: BaseModelModify) -> None:
        pass

    @staticmethod
    def generate_router(prefix: str, tags: [str]) -> fastapi.APIRouter:
        return fastapi.APIRouter(prefix=prefix, tags=tags)

    def generate_get_router(self):
        pass
    