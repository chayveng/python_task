
from fastapi import FastAPI

from tasks import example_task, show_text, stop_task
import json
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/read")
async def read():
    file_path = os.path.join("./target.json")
    try:
        with open(file_path, "r") as file:
            data = json.load(file)  # Directly parse the JSON data from the file
    except FileNotFoundError:
        return {"error": "File not found"}
    except json.JSONDecodeError:
        return {"error": "File is not a valid JSON"}
    except Exception as e:
        return {"error": str(e)}

    return {"data": data}


@app.get("/task")
async def task():
    task = example_task.delay(10, 20)  
    print(task)
    return {"message": "Task Executed", "task_id": task.task_id}

@app.post("/show_text")
async def show_text_(req: dict = {}):
    task = show_text.delay(req["interval"], req["value"])  
    print(task)
    return {"message": "Task Executed", "task_id": task.task_id}


@app.post("/stop_task")
async def stop(req: dict = {}):
    print(req["task_id"])
    stop_task(req["task_id"])
    return {"task_id": req["task_id"]}
    
    # task = show_text.delay(req["interval"], req["value"])  
    # print(task)
    # return {"message": "Task Executed", "task_id": task.task_id}

