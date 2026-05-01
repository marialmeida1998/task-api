from uuid import UUID

from fastapi import APIRouter, HTTPException, Response, status

from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])

_task_repository = TaskRepository()
_priority_advisor = PriorityAdvisor()
_task_service = TaskService(
    repository=_task_repository,
    priority_advisor=_priority_advisor,
)


@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate) -> TaskOut:
    return _task_service.create(task_create)


@router.get("", response_model=list[TaskOut], status_code=status.HTTP_200_OK)
def list_tasks() -> list[TaskOut]:
    return _task_service.list()


@router.get("/{task_id}", response_model=TaskOut, status_code=status.HTTP_200_OK)
def get_task(task_id: UUID) -> TaskOut:
    task = _task_service.get_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.put("/{task_id}", response_model=TaskOut, status_code=status.HTTP_200_OK)
def update_task(task_id: UUID, task_update: TaskUpdate) -> TaskOut:
    task = _task_service.update(task_id, task_update)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID) -> Response:
    deleted = _task_service.delete(task_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)
