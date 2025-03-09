import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.routers import router 

app = FastAPI()
app.include_router(router)

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_registration(client):
    response = client.post("/registration", json={"username": "John", "password": "password123"})
    assert response.status_code == 200
    assert response.json()["message"] == "registration successful"

def test_get_users(client):
    response = client.get("/get-users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_upload_user_data(client):
    csv_data = "Password,City,Age,Hobby\n123,NewCity,30,Football"
    response = client.post("/upload/Tom", json={"data": csv_data})
    assert response.status_code == 200
    assert response.json()["message"]["City"] == "NewCity"

def test_get_information(client):
    response = client.get("/get_information/Tom")
    assert response.status_code == 200
    assert response.json()["message"]["City"] == "NewCity" 

def test_registration_duplicate(client):
    client.post("/registration", json={"username": "Tom", "password": "password123"})
    response = client.post("/registration", json={"username": "Tom", "password": "password123"})
    assert response.status_code == 400
    assert response.json()["detail"] == "This user already exists"
