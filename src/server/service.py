import fastapi
from src.server.database.models import BaseModel
from src.server.database.pydantic_models import BaseModelModify
from typing import Type


class RouterManager:
    def __init__(self, database_model: Type[BaseModel], pydantic_model: Type[BaseModelModify], prefix: str, tags: [str]) -> None:
        self.database_model: Type[BaseModel] = database_model
        self.pydantic_model: Type[BaseModelModify] = pydantic_model
        self.fastapi_router: fastapi.APIRouter = fastapi.APIRouter(prefix=prefix, tags=tags)
        self.resolver_manager = ResolverManager(self.database_model, self.pydantic_model)
        self.init_routers()

    def init_routers(self):
        @self.fastapi_router.get('/get_all', response_model=list[self.pydantic_model])
        def generate_get_all_router():
            return self.resolver_manager.generate_get_all_resolve()

        @self.fastapi_router.get('/get/{id}', response_model=self.pydantic_model)
        def get(id: int):
            return self.resolver_manager.generate_get_resolve(id)


class ResolverManager:
    def __init__(self, database_model: Type[BaseModel], pydantic_model: Type[BaseModelModify]):
        self.database_model: Type[BaseModel] = database_model
        self.pydantic_model: Type[BaseModelModify] = pydantic_model

    def generate_get_all_resolve(self):
        return self.database_model.select()

    def generate_get_resolve(self, id: int):
        return self.database_model.get(self.database_model.id == id)