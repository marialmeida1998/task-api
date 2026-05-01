from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.api import task_routes
from app.main import app
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    isolated_service = TaskService(
        repository=TaskRepository(),
        priority_advisor=PriorityAdvisor(),
    )

    monkeypatch.setattr(task_routes, "_task_service", isolated_service)

    return TestClient(app)


def test_create_task_returns_201(client: TestClient) -> None:
    response = client.post(
        "/tasks",
        json={
            "title": "Criar rota de tarefas",
            "description": "Implementar endpoint de criacao",
            "priority": "media",
            "assignee": "Equipe API",
        },
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Criar rota de tarefas"
    assert response.json()["status"] == "pendente"


def test_list_tasks_returns_200(client: TestClient) -> None:
    client.post("/tasks", json={"title": "Primeira tarefa"})
    client.post("/tasks", json={"title": "Segunda tarefa"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_task_by_id_returns_200(client: TestClient) -> None:
    created_response = client.post("/tasks", json={"title": "Consultar tarefa"})
    task_id = created_response.json()["id"]

    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Consultar tarefa"


def test_update_task_returns_200(client: TestClient) -> None:
    created_response = client.post("/tasks", json={"title": "Tarefa original"})
    task_id = created_response.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Tarefa atualizada",
            "status": "em_andamento",
            "priority": "alta",
        },
    )

    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Tarefa atualizada"
    assert response.json()["status"] == "em_andamento"
    assert response.json()["priority"] == "alta"


def test_delete_task_returns_204(client: TestClient) -> None:
    created_response = client.post("/tasks", json={"title": "Remover tarefa"})
    task_id = created_response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204
    assert response.content == b""


def test_get_task_by_unknown_id_returns_404(client: TestClient) -> None:
    response = client.get(f"/tasks/{uuid4()}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_update_task_by_unknown_id_returns_404(client: TestClient) -> None:
    response = client.put(
        f"/tasks/{uuid4()}",
        json={"title": "Tarefa inexistente"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_delete_task_by_unknown_id_returns_404(client: TestClient) -> None:
    response = client.delete(f"/tasks/{uuid4()}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
