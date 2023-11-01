from src.server.routers import user as user

routers = (user.router_manager.fastapi_router, )