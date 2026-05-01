from datetime import datetime
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class TaskStatus(StrEnum):
    PENDING = "pendente"
    IN_PROGRESS = "em_andamento"
    DONE = "concluida"
    CANCELED = "cancelada"


class TaskPriority(StrEnum):
    LOW = "baixa"
    MEDIUM = "media"
    HIGH = "alta"
    CRITICAL = "critica"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=1000)
    priority: TaskPriority = TaskPriority.MEDIUM
    assignee: str | None = Field(default=None, max_length=120)


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=1000)
    status: TaskStatus | None = None
    priority: TaskPriority | None = None
    assignee: str | None = Field(default=None, max_length=120)


class TaskOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: str | None
    status: TaskStatus
    priority: TaskPriority
    assignee: str | None
    created_at: datetime
    updated_at: datetime
