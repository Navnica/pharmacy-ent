from src.server.router import routers
from src.server.database.pydantic_models import LoginData
from fastapi import FastAPI
from src.server.advanced.resolvers import user


user_router: FastAPI = routers[0]


@user_router.post('/login', response_model=int | None)
def login(login_data: LoginData):
    return user.login(login_data)
