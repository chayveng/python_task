import logging

from celery import Celery

# Configure the basic logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

celery = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0'
)

@celery.task(name='example_task')
def example_task(x, y):
    print("run example_task")
    try:
        logging.info("Running example_task")
        return x + y
    except Exception as e:
        logging.error(f"Error in example_task: {str(e)}")
        raise e
