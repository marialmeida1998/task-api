from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI

app = FastAPI(title="Task Prioritization API")


@app.get("/health")
def health_check() -> dict[str, Any]:
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
