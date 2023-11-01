import fastapi
from src.server.database.models import User
from src.server.database.pydantic_models import User as UserPydanticModel
from src.server.service import *

router_manager = RouterManager(
    database_model=User,
    pydantic_model=UserPydanticModel,
    prefix='/user',
    tags=['User']
)