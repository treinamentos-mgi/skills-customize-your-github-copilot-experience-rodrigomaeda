from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    # TODO: Return all tasks.
    return tasks


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    # TODO: Assign a unique ID, save the task, and return it.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this endpoint",
    )


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int) -> Task:
    # TODO: Return the matching task or raise a 404 error.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this endpoint",
    )


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate) -> Task:
    # TODO: Update the matching task or raise a 404 error.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this endpoint",
    )


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> None:
    # TODO: Delete the matching task or raise a 404 error.
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this endpoint",
    )
