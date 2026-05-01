from uuid import uuid4

import pytest

from app.models.task import TaskCreate, TaskPriority, TaskStatus, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService


@pytest.fixture
def task_service() -> TaskService:
    return TaskService(
        repository=TaskRepository(),
        priority_advisor=PriorityAdvisor(),
    )


def test_create_task_returns_task_with_default_status(task_service: TaskService) -> None:
    task = task_service.create(
        TaskCreate(
            title="Criar endpoint de tarefas",
            description="Implementar fluxo principal do MVP",
            priority=TaskPriority.MEDIUM,
            assignee="Equipe API",
        )
    )

    assert task.title == "Criar endpoint de tarefas"
    assert task.description == "Implementar fluxo principal do MVP"
    assert task.priority == TaskPriority.MEDIUM
    assert task.status == TaskStatus.PENDING
    assert task.assignee == "Equipe API"
    assert task.created_at == task.updated_at


def test_list_tasks_returns_created_tasks(task_service: TaskService) -> None:
    first_task = task_service.create(TaskCreate(title="Primeira tarefa"))
    second_task = task_service.create(TaskCreate(title="Segunda tarefa"))

    tasks = task_service.list()

    assert tasks == [first_task, second_task]


def test_get_by_id_returns_existing_task(task_service: TaskService) -> None:
    task = task_service.create(TaskCreate(title="Consultar tarefa"))

    found_task = task_service.get_by_id(task.id)

    assert found_task == task


def test_get_by_id_returns_none_when_task_does_not_exist(
    task_service: TaskService,
) -> None:
    found_task = task_service.get_by_id(uuid4())

    assert found_task is None


def test_update_task_changes_fields_and_updated_at(task_service: TaskService) -> None:
    task = task_service.create(
        TaskCreate(
            title="Tarefa original",
            description="Descricao original",
            priority=TaskPriority.LOW,
        )
    )

    updated_task = task_service.update(
        task.id,
        TaskUpdate(
            title="Tarefa atualizada",
            description="Descricao atualizada",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.HIGH,
            assignee="Equipe Produto",
        ),
    )

    assert updated_task is not None
    assert updated_task.id == task.id
    assert updated_task.title == "Tarefa atualizada"
    assert updated_task.description == "Descricao atualizada"
    assert updated_task.status == TaskStatus.IN_PROGRESS
    assert updated_task.priority == TaskPriority.HIGH
    assert updated_task.assignee == "Equipe Produto"
    assert updated_task.created_at == task.created_at
    assert updated_task.updated_at >= task.updated_at


def test_update_task_returns_none_when_task_does_not_exist(
    task_service: TaskService,
) -> None:
    updated_task = task_service.update(
        uuid4(),
        TaskUpdate(title="Tarefa inexistente"),
    )

    assert updated_task is None


def test_delete_task_removes_existing_task(task_service: TaskService) -> None:
    task = task_service.create(TaskCreate(title="Remover tarefa"))

    deleted = task_service.delete(task.id)

    assert deleted is True
    assert task_service.get_by_id(task.id) is None
    assert task_service.list() == []


def test_delete_task_returns_false_when_task_does_not_exist(
    task_service: TaskService,
) -> None:
    deleted = task_service.delete(uuid4())

    assert deleted is False
