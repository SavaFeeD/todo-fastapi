from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import response
from starlette import status


def clear(data):
    if type(data) == list:
        data = list(map(lambda x: x.to_dict(), data))
    else:
        data = data.to_dict()
    return data


def get_dashboard(db: Session, dashboard_id: int):
    return clear(db.query(models.Dashboard).filter(models.Dashboard.id == dashboard_id).first())


def get_dashboard_all(db: Session, offset: int, limit: int):
    return clear(db.query(models.Dashboard).offset(offset).limit(limit).all())


def create_dashboard(db: Session, dashboard: schemas.DashboardCreate):
    db_dashboard = models.Dashboard(**dashboard.dict())

    db.add(db_dashboard)
    db.commit()
    db.refresh(db_dashboard)

    return clear(db_dashboard)


def get_task(db: Session, task_id: int):
    return clear(db.query(models.Task).filter(models.Task.id == task_id).first())


def create_task(db: Session, task: schemas.TaskCreate, dashboard_id: int):
    db_task = models.Task(**task.dict(), dashboard_id=dashboard_id)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return clear(db_task)
