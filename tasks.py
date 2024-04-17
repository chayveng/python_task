import logging

from celery import Celery

# Configure the basic logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery.task(name='example_task')
def example_task(x, y):
    logger = logging.getLogger(__name__)
    logger.info("Running example_task multiple times")
    return x + y

