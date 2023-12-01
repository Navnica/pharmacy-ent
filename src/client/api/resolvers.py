import requests
from requests import Response
import json
import settings

server_url: str = f'http://{settings.SERVER_HOST}:{settings.SERVER_PORT}'


def server_available(func):
    def need_it(*args, **kwargs):
        try:
            requests.get(url=server_url)
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            return {'error': 'Server not available'}

    return need_it


@server_available
def register(fullname: str, login: str, password: str) -> dict:
    data = [('id', 0)]
    data = f'{{"id": 0, "fullname": "{fullname}", "balance": 100, "regular": false}}'

    return requests.post(
        url=f'{server_url}/user/create',
        data=data
    ).json()


@server_available
def login(login_str: str, password: str) -> int:
    data = {'login': login_str, 'password': password}

    answer = requests.post(
        url=f'{server_url}/auth_data/login',
        data=json.dumps(data)
    )

    print(answer.text)

    return 1
