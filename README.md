# ApolloFastapi

## Introduction

ApolloFastapi is a FastAPI-based web application designed for scraping search results from Apollo.io. This project provides a RESTful API that allows users to initiate a scraping job by providing a name and an organization name. The scraped results can be retrieved using a job ID generated upon job submission.

## Tech Stack

- FastAPI: FastAPI is used to build the web application and handle API requests.
- Celery: Celery is used for task queue management to handle background jobs.
- Redis: Redis is used as the message broker for Celery.
- Pydantic: Pydantic is used for data validation and serialization.
- Requests: Requests is used for making HTTP requests to scrape data.
- Python-dotenv: Python-dotenv is used for environment variable management.
- Pytz: Pytz is used for timezone management.
- Httpx: Httpx is used for fetching HTTPS responses.
- Docker: Docker is used for containerizing the application.
- Pytest: Pytest is used for testing the application.

## Installation Instructions

### Prerequisites

- Python 3.9 or higher
- Redis server

### Steps to Install and Run the Project

1. **Install Required Packages**
in terminal use:
pip install celery redis requests python-dotenv pytz httpx pytest docker

2. Install Project Dependencies
  -pip install -r requirements.txt
   
4. Run FastAPI Application
  - uvicorn apollo.main:app --reload
    
5. Run Celery Worker
  -celery -A apollo.celery_worker worker --loglevel=info

6. Run Tests
  -pytest tests/ or pytest

7.  Docker Instructions
  Build Docker Image
    - docker build -t myimage
  
  Run Docker Container
    - docker run -p 9090:80 myimage
    
8. Conventions and Development Details
  Directory Structure:
    - apollo: Contains the main FastAPI application code.
    - main.py: Main FastAPI application.
    - models.py: Pydantic models.
    - schemas.py: Pydantic schemas.
    - routes.py: FastAPI routes.
    - celery_worker.py: Celery worker configuration.
    - tests: Directory for unit tests.
    - test_app.py: Unit tests for the FastAPI application.
    - tasks.py: Celery task file for background job processing.
    - Dockerfile: Dockerfile for containerizing the application.
    - docker-compose.yml: Docker Compose file for defining and running multi-container Docker applications.
    - requirements.txt: Project dependencies.
