import requests
import time
from decouple import config
from typing import Dict,List,Optional, Any
from .cache import get_cached, set_cached


COINGECKO_BASE = config('COINGECKO_API_URL')

COIN_LIST_CACHE_TTL = int(config('COIN_LIST_CACHE_TTL'))
COIN_DETAIL_CACHE_TTL = int(config('COIN_DETAIL_CACHE_TTL'))
COIN_CHART_CACHE_TTL = int(config("COIN_CHART_CACHE_TTL")) 

def _safe_get (endpoint, params: dict = None, retries: int = 2, waitimer: float = 1.0 ) -> Optional[dict]:
    for attempt in range(retries + 1):
        try:
            response = requests.get(endpoint, params=params, timeout=10) 
            if response.status_code == 200: #retorna o json se a requisição der certo
                return response.json()
            elif response.status_code == 429: #em caso de excesso de requisições.
                time.sleep(waitimer * (attempt + 1))
            else: #se nenhum dos status code acima retorna None
                return None
        except requests.RequestException:
            time.sleep(waitimer * (attempt + 1))
    return None
        

def get_top_coins (per_page: int = 20,vs_currency: str = 'usd',page:int = 1) -> List[Dict]:


    cache_key = f'coins:top:{vs_currency}:page:{page}:per:{per_page}'
    cached = get_cached(cache_key)


    url = f'{COINGECKO_BASE}/coins/markets'
    params = {
        'vs_currency': vs_currency,
        'order': 'market_cap_desc',
        'per_page': per_page,
        'page': page,
        'sparkline': 'false',
        'price_change_percentage': '24h',
    }


    response = _safe_get(url, params=params)

    if response is None:

        if cached:
            return cached
        return []
    
    set_cached(cache_key, response, ttl=COIN_LIST_CACHE_TTL)
    return response



def get_coin_detail (coin_id: str, vs_currency: str = 'usd') -> Optional[Dict]:
    cache_key = f'coins:detail:{coin_id}:{vs_currency}'
    cached = get_cached(cache_key)

    url = f'{COINGECKO_BASE}/coins/{coin_id}'
    params = {
                'localization': 'false',
                'tickers': 'false',
                'market_data': 'true',
                'community_data': 'false',
                'developer_data': 'false',
                'sparkline': 'false'
                }

    response = _safe_get(url, params=params)

    if response is None:
        if cached:
            return cached
        return None

    set_cached(cache_key, response, ttl=COIN_DETAIL_CACHE_TTL)
    return response




def get_coin_chart(coin_id: str, vs_currency: str = "usd", days: int = 7) -> Optional[Dict[str, Any]]:
    """
    Retorna o histórico de preços de uma moeda em determinado número de dias.
    """
    cache_key = f"coins:chart:{coin_id}:{vs_currency}:{days}"
    cached = get_cached(cache_key)
    if cached:
        return cached

    url = f"{COINGECKO_BASE}/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days}

    data = _safe_get(url, params=params)
    if not data:
        return None

    set_cached(cache_key, data, ttl=COIN_CHART_CACHE_TTL)
    return data