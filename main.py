from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette import status

from app.dependencies import response
from app.database import engine
from app.routers import dashboards, tasks

from dotenv import load_dotenv

from app import models

# DATA BASE init
models.Base.metadata.create_all(bind=engine)


load_dotenv()

app = FastAPI()

app.mount('/static', StaticFiles(directory='./app/static'), name='static')

app.include_router(dashboards.router)
app.include_router(tasks.router)


@app.get('/')
async def index():
    return response(
        result={
            'msg': 'Hi! this is To-do app'
        },
        status=status.HTTP_200_OK
    )
