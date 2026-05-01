from uuid import UUID

from app.models.task import TaskCreate, TaskOut, TaskUpdate
from app.repositories.task_repository import TaskRepository
from app.services.priority_advisor import PriorityAdvisor


class TaskService:
    def __init__(
        self,
        repository: TaskRepository,
        priority_advisor: PriorityAdvisor,
    ) -> None:
        self._repository = repository
        self._priority_advisor = priority_advisor

    def create(self, task_create: TaskCreate) -> TaskOut:
        suggested_priority = self._priority_advisor.suggest(task_create)
        task_with_priority = task_create.model_copy(
            update={"priority": suggested_priority}
        )

        return self._repository.create(task_with_priority)

    def list(self) -> list[TaskOut]:
        return self._repository.list()

    def get_by_id(self, task_id: UUID) -> TaskOut | None:
        return self._repository.get_by_id(task_id)

    def update(self, task_id: UUID, task_update: TaskUpdate) -> TaskOut | None:
        if task_update.priority is None:
            current_task = self._repository.get_by_id(task_id)

            if current_task is None:
                return None

            suggested_priority = self._priority_advisor.suggest_update(
                current_task=current_task,
                task_update=task_update,
            )
            task_update = task_update.model_copy(
                update={"priority": suggested_priority}
            )

        return self._repository.update(task_id, task_update)

    def delete(self, task_id: UUID) -> bool:
        return self._repository.delete(task_id)
