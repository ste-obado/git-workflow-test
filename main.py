from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="CI Practice API", version="1.0.0")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


# Simple in-memory storage for learning.
tasks: dict[int, Task] = {}
next_id = 1


@app.get("/")
def home():
    return {"message": "Welcome to the CI Practice API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    global next_id

    task = Task(id=next_id, **task_data.model_dump())
    tasks[next_id] = task
    next_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
