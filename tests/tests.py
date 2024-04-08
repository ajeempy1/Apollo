import pytest
from starlette.testclient import TestClient
from apollo.main import app  # Importing app from apollo app

client = TestClient(app)


def test_create_scrape_job():
    response = client.post("/scrape/", json={"name": "Ajeem", "organization_name": "Worthyprogress"})
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_scrape_results():
    response = client.post("/scrape/", json={"name": "Ajeem", "organization_name": "Worthyprogress"})
    job_id = response.json()["job_id"]

    response = client.get("/scrape/" + job_id)
    assert response.status_code == 200
    assert "status" in response.json()
    assert "results" in response.json()
