from fastapi import FastAPI
from enum import Enum # makes code easier to maintain and endpoints have more efficient checks
from src.schemas import TaskBase

app = FastAPI()

# CREATE
@app.post("/tasks/create/")
async def create_task(task: TaskBase):
    return task

# READ
# @app.get("/tasks/{task_id}")
# async def get_task(task_id: int):

#     return {"task_id": task_id}

# READ ALL
# @app.get("/tasks/")
# async def get_tasks()
#     return all_tasks

# UPDATE

# DELETE
