from sqlalchemy import select
from sqlalchemy.orm import Session

from .db_models import Task
from .models import TaskCreate, TaskUpdate


class TaskStorage:

    @staticmethod
    def create(db: Session, data: TaskCreate):
        task = Task(
            title=data.title,
            description=data.description,
        )

        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    @staticmethod
    def get_all(db: Session):
        statement = select(Task).order_by(Task.id)

        return db.scalars(statement).all()

    @staticmethod
    def get(db: Session, task_id: int):
        return db.get(Task, task_id)

    @staticmethod
    def update(
        db: Session,
        task: Task,
        data: TaskUpdate,
    ):
        updates = data.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(task, key, value)

        db.commit()
        db.refresh(task)

        return task

    @staticmethod
    def delete(db: Session, task: Task):
        db.delete(task)
        db.commit()
