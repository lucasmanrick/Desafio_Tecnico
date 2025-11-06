from celery import shared_task
from .services.coingecko import get_top_coins
from .services.cache import set_cached
import os

COIN_LIST_CACHE_TTL = int(os.getenv('COIN_LIST_CACHE_TTL'))

@shared_task(bind=True, max_retries=3)
def update_coin_prices_cache():
    vs_currency = 'usd'
    per_page = 20
    total = 100
    pages = total // per_page

    for page in range(1, pages + 1):
        data = get_top_coins(limit=per_page, vs_currency=vs_currency, page=page)
        cache_key = f'coins:top:{vs_currency}:page:{page}:per:{per_page}'
        set_cached(cache_key, data, ttl=COIN_LIST_CACHE_TTL)