from src.server.database.models import AuthData
from src.server.database.pydantic_models import LoginData


def login(login_data: LoginData):
    auth_data: AuthData = AuthData.get_or_none(
        AuthData.login == login_data.login,
        AuthData.password == login_data.password
    )

    return AuthData if auth_data is None else auth_data.user_id.id


