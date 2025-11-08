# utils/health_check.py
from django.db import connections
from django.db.utils import OperationalError
import requests

def check_database_connection() -> bool:
    try:
        connections['default'].cursor()
        return True
    except Exception:
        return False


def check_coingecko_api() -> bool:
    try:
        resp = requests.get("https://api.coingecko.com/api/v3/ping", timeout=5)
        return resp.status_code == 200
    except Exception:
        return False
