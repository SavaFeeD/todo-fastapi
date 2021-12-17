from fastapi import APIRouter, Depends
from typing import Optional
from starlette import status
from sqlalchemy.orm import Session

from app.dependencies import response, get_db

from app import models, schemas, crud


router = APIRouter(
    prefix='/dashboards',
    tags=['todo', 'dashboards'],
    responses={404: {'descriptions': 'Not found'}}
)


@router.get('/all')
async def get_all(offset: Optional[int] = 0, limit: Optional[int] = 10, db: Session = Depends(get_db)):
    if offset > limit:
        return response(
            error='Offset must be less than the limit',
            status=status.HTTP_400_BAD_REQUEST
        )
    dashboards = crud.get_dashboard_all(db)
    return response(
        result={
            "list": dashboards
        },
        status=status.HTTP_200_OK
    )
