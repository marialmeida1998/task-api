import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.models.task import TaskCreate, TaskOut, TaskPriority, TaskUpdate


class PriorityAdvisor:
    _OPENAI_RESPONSES_URL = "https://api.openai.com/v1/responses"
    _DEFAULT_MODEL = "gpt-5.4-nano"
    _DEFAULT_TIMEOUT_SECONDS = 3.0

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        timeout_seconds: float = _DEFAULT_TIMEOUT_SECONDS,
    ) -> None:
        self._api_key = api_key or os.getenv("OPENAI_API_KEY")
        self._model = model or os.getenv("OPENAI_MODEL", self._DEFAULT_MODEL)
        self._timeout_seconds = timeout_seconds

    def suggest(self, task_create: TaskCreate) -> TaskPriority:
        local_priority = self._suggest_locally(
            title=task_create.title,
            description=task_create.description,
            fallback=task_create.priority,
        )

        return self._suggest_with_fallback(
            title=task_create.title,
            description=task_create.description,
            fallback=local_priority,
        )

    def suggest_update(
        self,
        current_task: TaskOut,
        task_update: TaskUpdate,
    ) -> TaskPriority:
        title = task_update.title if task_update.title is not None else current_task.title
        description = (
            task_update.description
            if task_update.description is not None
            else current_task.description
        )

        local_priority = self._suggest_locally(
            title=title,
            description=description,
            fallback=current_task.priority,
        )

        return self._suggest_with_fallback(
            title=title,
            description=description,
            fallback=local_priority,
        )

    def _suggest_with_fallback(
        self,
        title: str,
        description: str | None,
        fallback: TaskPriority,
    ) -> TaskPriority:
        if not self._api_key:
            return fallback

        try:
            llm_priority = self._suggest_with_llm(
                title=title,
                description=description,
            )
        except (HTTPError, URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError):
            return fallback

        return llm_priority or fallback

    def _suggest_locally(
        self,
        title: str,
        description: str | None,
        fallback: TaskPriority,
    ) -> TaskPriority:
        text = self._build_text(title, description)

        if self._has_critical_terms(text):
            return TaskPriority.CRITICAL

        if self._has_high_priority_terms(text):
            return TaskPriority.HIGH

        if self._has_low_priority_terms(text):
            return TaskPriority.LOW

        return fallback

    def _suggest_with_llm(
        self,
        title: str,
        description: str | None,
    ) -> TaskPriority | None:
        request = Request(
            self._OPENAI_RESPONSES_URL,
            data=json.dumps(self._build_llm_payload(title, description)).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )

        with urlopen(request, timeout=self._timeout_seconds) as response:
            payload = json.loads(response.read().decode("utf-8"))

        response_text = self._extract_response_text(payload)
        return self._parse_priority(response_text)

    def _build_llm_payload(self, title: str, description: str | None) -> dict[str, object]:
        return {
            "model": self._model,
            "instructions": (
                "Classifique a prioridade da tarefa para uma equipe interna. "
                "Responda apenas com um destes valores: baixa, media, alta, critica."
            ),
            "input": (
                f"Titulo: {title}\n"
                f"Descricao: {description or ''}\n"
                "Prioridade:"
            ),
            "max_output_tokens": 10,
        }

    def _extract_response_text(self, payload: dict[str, object]) -> str:
        output_text = payload.get("output_text")

        if isinstance(output_text, str):
            return output_text

        output = payload.get("output")

        if not isinstance(output, list):
            return ""

        chunks: list[str] = []

        for item in output:
            if not isinstance(item, dict):
                continue

            content = item.get("content")

            if not isinstance(content, list):
                continue

            for content_item in content:
                if not isinstance(content_item, dict):
                    continue

                text = content_item.get("text")

                if isinstance(text, str):
                    chunks.append(text)

        return " ".join(chunks)

    def _parse_priority(self, value: str) -> TaskPriority | None:
        normalized_value = value.strip().lower()

        for priority in TaskPriority:
            if priority.value in normalized_value:
                return priority

        return None

    def _build_text(self, title: str, description: str | None) -> str:
        return f"{title} {description or ''}".lower()

    def _has_critical_terms(self, text: str) -> bool:
        critical_terms = ("critico", "critica", "urgente", "bloqueio", "incidente")
        return any(term in text for term in critical_terms)

    def _has_high_priority_terms(self, text: str) -> bool:
        high_priority_terms = ("alta", "importante", "risco", "prazo")
        return any(term in text for term in high_priority_terms)

    def _has_low_priority_terms(self, text: str) -> bool:
        low_priority_terms = ("baixa", "quando der", "sem urgencia", "baixa prioridade")
        return any(term in text for term in low_priority_terms)
