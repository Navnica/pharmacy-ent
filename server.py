import uvicorn
import fastapi
import settings


app = fastapi.FastAPI(
    title='PharmancyEnt api',
    version='0.1 Startis',
    description='PharamancyEntAPI - PharamancyEnt Application Programming Interface'
)


@app.get('/', include_in_schema=False)
def index() -> fastapi.responses.RedirectResponse:
    return fastapi.responses.RedirectResponse('/docs')


if __name__ == '__main__':
    if settings.DEBUG:
        from src.server.database.dbfill import dbfill
        dbfill()

    uvicorn.run('server:app', reload=True, host=settings.SERVER_HOST, port=settings.SERVER_PORT)