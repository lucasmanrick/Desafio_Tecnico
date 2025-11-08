from django.db import connections
from django.conf import settings
import requests
import redis

def check_database_connection() -> bool:
    try:
        connections['default'].cursor()
        return True
    except Exception:
        return False


def check_coingecko_api() -> bool:
    try:
        resp = requests.get("https://api.coingecko.com/api/v3/ping", timeout=5)
        return True if resp.status_code == 200 else False
    except Exception:
        return False
    
def check_redis_connection() -> bool:
    try:
        r = redis.Redis.from_url(settings.CELERY_BROKER_URL, socket_connect_timeout=2)
        r.ping()
        return True
    except Exception:
        return False

def check_celery_worker() -> str:
    try:
        from celery import current_app
        insp = current_app.control.inspect()
        active = insp.active()
        return True if active else False
    except Exception:
        return False


def verify_health() -> dict:
      db= check_database_connection() 
      coingecko = check_coingecko_api()
      redis = check_redis_connection()
      celery_worker = check_celery_worker()
      
      return {"status": "healthy" if db and coingecko else "unhealthy", 
              "checks": {
                  "database": "ok" if db else "error",
                  "redis": "ok" if redis else "error",
                  "celery": "ok" if celery_worker else "error",
                  "coingecko_api": "ok" if coingecko else "error"
              }
              
              }  