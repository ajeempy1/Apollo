from fastapi import FastAPI
from apollo.routes import router as scrape_router

app = FastAPI()

app.include_router(scrape_router, prefix="/scrape", tags=["scrape"])
