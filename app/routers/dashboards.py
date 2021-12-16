from fastapi import APIRouter

from starlette import status

from app.dependencies import response

from typing import Optional


router = APIRouter(
    prefix='/dashboards',
    tags=['todo', 'dashboards'],
    responses={404: {'descriptions': 'Not found'}}
)


@router.get('/all')
async def get_all(offset: Optional[int] = 0, limit: Optional[int] = 10):
    if offset > limit:
        return response(
            error='Offset must be less than the limit',
            status=status.HTTP_400_BAD_REQUEST
        )
    return response(
        result={
            'offset': offset,
            'limit': limit
        },
        status=status.HTTP_200_OK
    )
