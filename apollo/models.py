from pydantic import BaseModel
from typing import Optional


class ScrapingJob(BaseModel):
    id: Optional[int] = None
    name: str
    organization_name: str
    status: str = 'in_progress'
    results: Optional[str] = None
