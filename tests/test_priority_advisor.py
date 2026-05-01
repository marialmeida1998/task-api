import pytest

from app.models.task import TaskCreate, TaskPriority
from app.services.priority_advisor import PriorityAdvisor


@pytest.fixture
def advisor(monkeypatch: pytest.MonkeyPatch) -> PriorityAdvisor:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    return PriorityAdvisor()


def test_suggest_returns_critical_priority_for_critical_terms(
    advisor: PriorityAdvisor,
) -> None:
    task = TaskCreate(
        title="Incidente urgente",
        description="Bloqueio critico em producao",
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.CRITICAL


def test_suggest_returns_high_priority_for_high_priority_terms(
    advisor: PriorityAdvisor,
) -> None:
    task = TaskCreate(
        title="Ajuste importante",
        description="Existe risco de perder o prazo",
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.HIGH


def test_suggest_returns_low_priority_for_low_priority_terms(
    advisor: PriorityAdvisor,
) -> None:
    task = TaskCreate(
        title="Melhoria sem urgencia",
        description="Pode ser feita quando der",
        priority=TaskPriority.MEDIUM,
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.LOW


def test_suggest_returns_input_priority_when_no_terms_match(
    advisor: PriorityAdvisor,
) -> None:
    task = TaskCreate(
        title="Revisar texto do README",
        description="Ajuste simples de documentacao",
        priority=TaskPriority.MEDIUM,
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.MEDIUM


def test_suggest_uses_local_fallback_when_llm_call_fails(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "invalid-key")

    advisor = PriorityAdvisor(timeout_seconds=0.001)

    task = TaskCreate(
        title="Risco importante",
        description="Pode afetar o prazo da entrega",
        priority=TaskPriority.MEDIUM,
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.HIGH
