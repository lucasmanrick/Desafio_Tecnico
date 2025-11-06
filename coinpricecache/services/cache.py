# coins/services/cache.py
import os
import json
import redis
from typing import Any, Optional

REDIS_URL = os.getenv('REDIS_URL', os.getenv('CELERY_BROKER_URL'))
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

def set_cached(key: str, value: Any, ttl: int = 120) -> None:
    payload = json.dumps(value)
    redis_client.setex(key, ttl, payload)

def get_cached(key: str) -> Optional[Any]:
    data = redis_client.get(key)
    if not data:
        return None
    try:
        return json.loads(data)
    except Exception:
        return None

def delete_cached(key: str) -> None:
    redis_client.delete(key)