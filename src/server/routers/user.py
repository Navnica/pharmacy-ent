import fastapi
from src.server.database.models import User
from src.server.database.pydantic_models import User as UserPydanticModel

router = fastapi.APIRouter(prefix='/user', tags=['User'])

