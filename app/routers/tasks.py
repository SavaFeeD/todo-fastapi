from fastapi import APIRouter, Depends
from typing import Optional
from starlette import status
from sqlalchemy.orm import Session

from app.dependencies import response, get_db

from app import schemas, crud


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
    responses={404: {'descriptions': 'Not Found'}}
)


@router.get('/{task_id}')
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = crud.get_task(db, task_id)

    return response(
        result={
            'task': task
        },
        status=status.HTTP_200_OK
    )


@router.post('/create')
def get_task(data: schemas.TaskCreate, dashboard_id: int, db: Session = Depends(get_db)):

    task = crud.create_task(db, data, dashboard_id)

    return response(
        result={
            'task': task
        },
        status=status.HTTP_200_OK
    )
