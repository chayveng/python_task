
from fastapi import FastAPI

from tasks import example_task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/task")
async def task():
    task = example_task.delay(10, 20)  
    print(task)
    return {"message": "Task Executed", "task_id": task.task_id}
