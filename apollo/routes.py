from fastapi import APIRouter, BackgroundTasks, HTTPException
from celery import Celery
from apollo.models import ScrapingJob
from apollo.schemas import ScrapeRequest, ScrapeResponse
from apollo.constant import *
import time

router = APIRouter()
celery_app = Celery("tasks", broker=REDIS_URL)

job_db = {}


@router.post("/", response_model=ScrapeResponse)
async def scrape(scrape_request: ScrapeRequest, background_tasks: BackgroundTasks):
    job_id = len(job_db) + 1  # Generate job ID based on the length of job_db
    background_tasks.add_task(run_scraping_task, job_id, scrape_request.name, scrape_request.organization_name)
    return {"job_id": job_id}


def run_scraping_task(job_id: int, name: str, organization_name: str):
    import time
    time.sleep(10)
    job_db[job_id] = {
        "status": "finished",
        "results": "Results for {} from {}".format(name, organization_name)
    }


@router.get("/{job_id}", response_model=ScrapingJob)
async def scrape_results(job_id: int):
    if job_id not in job_db:
        raise HTTPException(status_code=404, detail="Job not found")

    job_data = job_db[job_id]
    job = ScrapingJob(
        id=job_id,
        name=job_data["results"].split(" ")[2],
        organization_name=job_data["results"].split(" ")[4],
        status=job_data["status"],
        results=job_data["results"]
    )
    return job
