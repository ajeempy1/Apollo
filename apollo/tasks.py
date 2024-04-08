from celery import Celery
from time import sleep
from .models import ScrapingJob

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def scrape_job(job: ScrapingJob):
    # Simulating a long-running task
    sleep(10)
    job.status = 'completed'
    job.results = f"Results for {job.name} from {job.organization_name}"
    return job
