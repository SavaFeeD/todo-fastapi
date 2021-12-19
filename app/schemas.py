from typing import Optional, List

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    dashboard_id: int
    is_active: bool

    class Config:
        orm_mode = True


class DashboardBase(BaseModel):
    name: str


class DashboardCreate(DashboardBase):
    pass


class Dashboard(DashboardBase):
    id: int
    tasks:  List[Task] = []

    class Config:
        orm_mode = True
