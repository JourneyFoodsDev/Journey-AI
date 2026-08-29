from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Any


def filled(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return len(value) > 0
    return True


def rate(rows: list[dict], fields: list[str]) -> dict:
    if not rows:
        return {"count": 0, "pct": 0, "missing": {f: 0 for f in fields}}
    missing = {f: 0 for f in fields}
    hits = 0
    total = len(rows) * max(len(fields), 1)
    for row in rows:
        for field in fields:
            if filled(row.get(field)):
                hits += 1
            else:
                missing[field] += 1
    return {
        "count": len(rows),
        "pct": round(100 * hits / total, 1) if total else 0,
        "missing": missing,
    }


def write_report(name: str, payload: dict) -> str:
    os.makedirs("out", exist_ok=True)
    path = os.path.join("out", f"{name}.json")
    payload["generatedAt"] = datetime.now(timezone.utc).isoformat()
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    return path
