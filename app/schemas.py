from typing import Optional, List

from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    is_active: bool
    dashboard_id: int

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
