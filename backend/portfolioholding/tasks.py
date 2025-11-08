import requests
from decimal import Decimal
from portfolioholding.models import PortfolioHolding
import os

COINGECKO_API_URL = os.getenv("COINGECKO_API_URL") 


def update_portfolio_prices(user_id: str):
    """
    Atualiza preços atuais e calcula lucro/prejuízo das holdings de um usuário.
    """

    holdings = PortfolioHolding.objects.filter(user_id=user_id)

    if not holdings.exists():
        return {"message": "Usuário não possui holdings."}

    coin_ids = ",".join(set(holdings.values_list("coin_id", flat=True)))

    response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids={coin_ids}&vs_currencies=usd")
    if response.status_code != 200:
        return {"error": "Falha ao consultar CoinGecko."}

    prices = response.json() 

    portfolio_data = []
    total_invested = Decimal("0")
    total_value = Decimal("0")
    total_profit = Decimal("0")

    for holding in holdings:
        coin_data = prices.get(holding.coin_id)
        if not coin_data:
            continue

        current_price = Decimal(coin_data["usd"]) #preço atual da coin
        invested_value = holding.amount * holding.purchase_price_usd #Valor que a pessoa tinha quando comprou
        current_value = holding.amount * current_price  #Valor que a pessoa tem agora
        profit_loss = current_value - invested_value
        profit_percentage = (profit_loss / invested_value)
        

        
        portfolio_data.append({
            "id": str(holding.id),
            "coin_id": holding.coin_id,
            "coin_name": holding.coin_name,
            "coin_symbol": holding.coin_symbol,
            "coin_image": holding.coin_image,
            "amount": float(holding.amount),
            "purchase_price_usd": float(holding.purchase_price_usd),
            "current_price_usd": float(current_price),
            "total_invested_usd": float(total_invested),
            "profit_usd": float(profit_loss),
            "profit_percentage": round(float(profit_percentage), 2),
            "current_value_usd": float(current_value),
            "purchase_date": holding.purchase_date.isoformat(),
            "created_at": holding.created_at.isoformat(),
            "updated_at": holding.updated_at.isoformat(),
        })

        total_invested += invested_value
        total_value += current_value

    total_profit = total_value - total_invested
    total_profit_percentage = (total_profit / total_invested * 100) if total_invested > 0 else 0
    
    return {
        "total_value_usd": round(float(total_value), 2),
        "total_invested_usd": round(float(total_invested), 2),
        "total_profit_usd": round(float(total_profit), 2),
        "total_profit_percentage": round(float(total_profit_percentage), 2),
        "holdings": portfolio_data
    }
