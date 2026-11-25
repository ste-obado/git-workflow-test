from fastapi.testclient import TestClient

from main import app, tasks

client = TestClient(app)


def setup_function():
    # Keep tests independent from one another.
    tasks.clear()


def test_home_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the CI Practice API"
    }


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_create_and_list_task():
    create_response = client.post(
        "/tasks",
        json={"title": "Learn GitHub Actions"}
    )

    assert create_response.status_code == 201
    created_task = create_response.json()
    assert created_task["id"] == 1
    assert created_task["title"] == "Learn GitHub Actions"
    assert created_task["completed"] is False

    list_response = client.get("/tasks")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1


def test_get_missing_task_returns_404():
    response = client.get("/tasks/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

def test_ci_detects_failure():
    assert 1 == 2
