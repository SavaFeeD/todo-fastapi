from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette import status

from app.routers import dashboards
from app.dependencies import response

from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

app.mount('/static', StaticFiles(directory='./app/static'), name='static')

app.include_router(dashboards.router)


@app.get('/')
async def index():
    return response(
        result={
            'msg': 'Hi! this is To-do app'
        },
        status=status.HTTP_200_OK
    )
