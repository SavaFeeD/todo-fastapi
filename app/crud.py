from sqlalchemy.orm import Session
from app import models, schemas


def get_dashboard(db: Session, dashboard_id: int):
    return db.query(models.Dashboard).filter(models.Dashboard.id == dashboard_id).first()


def get_dashboard_all(db: Session):
    return db.query(models.Dashboard).all()


def create_dashboard(db: Session, dashboard: schemas.DashboardCreate):
    db_dashboard = models.Dashboard(**dashboard.dict())

    db.add(db_dashboard)
    db.commit()
    db.refresh(db_dashboard)

    return db_dashboard


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task
