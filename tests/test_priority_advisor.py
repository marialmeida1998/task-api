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


def test_suggest_uses_llm_priority_when_available(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")

    advisor = PriorityAdvisor()

    def fake_suggest_with_llm(title: str, description: str | None) -> TaskPriority:
        return TaskPriority.CRITICAL

    monkeypatch.setattr(advisor, "_suggest_with_llm", fake_suggest_with_llm)

    task = TaskCreate(
        title="Tarefa simples",
        description="Sem termos de prioridade local",
        priority=TaskPriority.LOW,
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.CRITICAL


def test_suggest_uses_local_fallback_when_llm_returns_none(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")

    advisor = PriorityAdvisor()

    def fake_suggest_with_llm(title: str, description: str | None) -> None:
        return None

    monkeypatch.setattr(advisor, "_suggest_with_llm", fake_suggest_with_llm)

    task = TaskCreate(
        title="Ajuste importante",
        description="Existe risco de perder o prazo",
        priority=TaskPriority.MEDIUM,
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.HIGH


def test_suggest_uses_local_fallback_when_llm_times_out(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")

    advisor = PriorityAdvisor()

    def fake_suggest_with_llm(title: str, description: str | None) -> TaskPriority:
        raise TimeoutError

    monkeypatch.setattr(advisor, "_suggest_with_llm", fake_suggest_with_llm)

    task = TaskCreate(
        title="Incidente urgente",
        description="Bloqueio no fluxo interno",
        priority=TaskPriority.MEDIUM,
    )

    priority = advisor.suggest(task)

    assert priority == TaskPriority.CRITICAL


def test_parse_priority_from_output_text() -> None:
    advisor = PriorityAdvisor()

    priority = advisor._parse_priority("Prioridade sugerida: critica")

    assert priority == TaskPriority.CRITICAL
