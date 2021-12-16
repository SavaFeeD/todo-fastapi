from sqlalchemy import Column, ForeignKey, Boolean, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Dashboard(Base):
    __tablename__ = 'dashboards'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    tasks = relationship("Task", back_populates="dashboard")


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    dashboard_id = Column(Integer, ForeignKey("dashboards.id"))

    dashboard = relationship("Dashboard", back_populates="tasks")
