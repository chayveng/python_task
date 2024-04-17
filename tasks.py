import logging
import time
import json
import os
from datetime import timedelta
from celery.schedules import crontab

from celery import Celery
from celery.app.control import Control

# Configure the basic logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

celery.conf.beat_schedule = {
    'run-my-task-every-minute': {
        'task': 'tasks.auto_start_task',
        'schedule': timedelta(seconds=10),  # Executes every minute
    },
}
# 'schedule': crontab(minute='*/1'),  # Executes every minute

celery.conf.update(
    enable_utc=True,
    timezone='UTC',
)


control = Control(app=celery)

@celery.task
def auto_start_task():
    print("Start Up Task !!")
    # file_path = os.path.join("./target.json")
    # try:
    #     with open(file_path, "r") as file:
    #         data = json.load(file)  # Directly parse the JSON data from the file
    # except FileNotFoundError:
    #     return {"error": "File not found"}
    # except json.JSONDecodeError:
    #     return {"error": "File is not a valid JSON"}
    # except Exception as e:
    #     return {"error": str(e)}

    # return {"data": data}
    

def stop_task(task_id):
    control.revoke(task_id, terminate=True)
    print("task_id:", task_id)


@celery.task(name='example_task')
def example_task(x, y):
    print("run example_task")
    try:
        logging.info("Running example_task")
        return x + y
    except Exception as e:
        logging.error(f"Error in example_task: {str(e)}")
        raise e

@celery.task(name="show_text")
def show_text(interval, value):
    while True:
        # print("text: {text}, interval: {interval}")
        print("text: {}".format(value))
        time.sleep(interval)

