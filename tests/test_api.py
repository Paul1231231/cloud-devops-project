from fastapi.testclient import TestClient

from cloud_devops_project.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn AWS",
            "description": "Study ECS and ECR",
        },
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Learn AWS"


def test_get_task_not_found():
    response = client.get("/tasks/999999")

    assert response.status_code == 404


def test_invalid_task():
    response = client.post(
        "/tasks",
        json={"title": ""},
    )

    assert response.status_code == 422
