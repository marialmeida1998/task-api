from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI

from app.api.task_routes import router as task_router

app = FastAPI(title="Task Prioritization API")

app.include_router(task_router)


@app.get("/health")
def health_check() -> dict[str, Any]:
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
