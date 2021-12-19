from fastapi import APIRouter, Depends
from typing import Optional
from starlette import status
from sqlalchemy.orm import Session

from app.dependencies import response, get_db

from app import schemas, crud


router = APIRouter(
    prefix='/dashboards',
    tags=['Dashboards'],
    responses={404: {'descriptions': 'Not found'}}
)


@router.get('/all')
def get_all(offset: Optional[int] = 0, limit: Optional[int] = 10, db: Session = Depends(get_db)):

    if offset > limit:
        return response(
            error='Offset must be less than the limit',
            status=status.HTTP_400_BAD_REQUEST
        )

    dashboards = crud.get_dashboard_all(db, offset,  limit)

    return response(
        result={
            'list': dashboards
        },
        status=status.HTTP_200_OK
    )


@router.get('/{dashboard_id}')
def get_dashboard(dashboard_id: int, db: Session = Depends(get_db)):

    dashboard = crud.get_dashboard(db, dashboard_id)

    return response(
        result={
            'dashboard': dashboard
        },
        status=status.HTTP_200_OK
    )


@router.post('/create')
def create_dashboard(data: schemas.DashboardCreate, db: Session = Depends(get_db)):
    new_dashboard = crud.create_dashboard(db, data)

    return response(
        result={
            'dashboard': new_dashboard
        },
        status=status.HTTP_200_OK
    )
