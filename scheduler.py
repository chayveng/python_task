from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'run-my-task-every-minute': {
        'task': 'tasks.my_periodic_task',
        'schedule': crontab(minute='*/1'),  # Executes every minute
    },
}

app.conf.update(
    enable_utc=True,
    timezone='UTC',
)
