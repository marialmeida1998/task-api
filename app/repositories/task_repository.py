from datetime import datetime, timezone
from uuid import UUID, uuid4

from app.models.task import TaskCreate, TaskOut, TaskStatus, TaskUpdate


class TaskRepository:
    def __init__(self) -> None:
        self._tasks: dict[UUID, TaskOut] = {}

    def create(self, task_create: TaskCreate) -> TaskOut:
        now = datetime.now(timezone.utc)

        task = TaskOut(
            id=uuid4(),
            title=task_create.title,
            description=task_create.description,
            status=TaskStatus.PENDING,
            priority=task_create.priority,
            assignee=task_create.assignee,
            created_at=now,
            updated_at=now,
        )

        self._tasks[task.id] = task
        return task

    def list(self) -> list[TaskOut]:
        return list(self._tasks.values())

    def get_by_id(self, task_id: UUID) -> TaskOut | None:
        return self._tasks.get(task_id)

    def update(self, task_id: UUID, task_update: TaskUpdate) -> TaskOut | None:
        current_task = self._tasks.get(task_id)

        if current_task is None:
            return None

        update_data = task_update.model_dump(exclude_unset=True)
        updated_task = current_task.model_copy(
            update={
                **update_data,
                "updated_at": datetime.now(timezone.utc),
            }
        )

        self._tasks[task_id] = updated_task
        return updated_task

    def delete(self, task_id: UUID) -> bool:
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True
