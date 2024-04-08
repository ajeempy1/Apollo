from celery import Celery
from apollo.constant import *

celery_app = Celery("tasks", broker="REDIS_URL")


@celery_app.task
def scrape_task(name: str, organization_name: str):
    import time
    time.sleep(10)

    return f"Results for {name} from {organization_name}"
