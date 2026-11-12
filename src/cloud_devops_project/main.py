from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from .database import Base, engine
from .dependencies import get_db
from .models import TaskCreate, TaskUpdate, TaskResponse
from .storage import TaskStorage

app = FastAPI(
    title="Cloud DevOps Task API",
    version="1.0.0",
)

storage = TaskStorage()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    request: TaskCreate,
    db: Session = Depends(get_db),
):
    return storage.create(db, request)


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return storage.get_all(db)


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = storage.get(db, task_id)

    if task is None:
        raise HTTPException(404, "Task not found")

    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    request: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = storage.get(db, task_id)

    if task is None:
        raise HTTPException(404, "Task not found")

    return storage.update(db, task, request)


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
):
    task = storage.get(db, task_id)

    if task is None:
        raise HTTPException(404, "Task not found")

    storage.delete(db, task)

    return Response(status_code=204)