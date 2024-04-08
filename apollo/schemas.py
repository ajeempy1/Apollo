from pydantic import BaseModel


class ScrapeRequest(BaseModel):
    name: str
    organization_name: str


class ScrapeResponse(BaseModel):
    job_id: str
