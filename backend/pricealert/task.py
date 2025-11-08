# alerts/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import PriceAlert
from notification.models import Notification
import requests

@shared_task
def check_price_alerts():

    alerts = PriceAlert.objects.filter(is_active=True, triggered=False)
    if not alerts.exists():
        return

    coin_ids = list(set(alerts.values_list("coin_id", flat=True)))
    ids_param = ",".join(coin_ids)

    try:   #PEGA O VALOR DE TODAS AS MOEDAS RETORNADAS NO ALERTS(MOEDAS FAVORITAS EXISTENTES ATUALMENTE).
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": ids_param, "vs_currencies": "usd"},
            timeout=10,
        )
        prices = response.json()
    except Exception as e:
        return

    for alert in alerts:  #pega o preço atual da moeda da pessoa que pediu o alerta.
        current_price = prices.get(alert.coin_id, {}).get("usd")
        if current_price is None: #se não tiver current_price passa para a proxima pessoa que pediu o alerta.
            continue

        # Verifica condição de disparo
        condition_hit = (
            (alert.condition == "above" and current_price >= float(alert.target_price_usd))
            or
            (alert.condition == "below" and current_price <= float(alert.target_price_usd))
        )

        if condition_hit: #se o alerta for emitido/atingir ao criterio que a pessoa pediu ativamos o alerta e desativamos o "listening" dessa analisa recorrente de atingimento do alerta.
            alert.triggered = True
            alert.is_active = False
            alert.triggered_at = timezone.now()
            alert.save(update_fields=["triggered", "is_active", "triggered_at"])

            # Cria a notificação com sua model
            Notification.objects.create(
                user=alert.user,
                type="price_alert",
                title=f"Alerta de preço atingido: {alert.coin_name}",
                message=(
                    f"O preço de {alert.coin_name} ({alert.coin_symbol.upper()}) "
                    f"{'subiu acima' if alert.condition == 'above' else 'caiu abaixo'} "
                    f"de ${alert.target_price_usd:.2f}. "
                    f"Preço atual: ${current_price:.2f}."
                ),
                data={
                    "coin_id": alert.coin_id,
                    "coin_name": alert.coin_name,
                    "coin_symbol": alert.coin_symbol,
                    "target_price_usd": float(alert.target_price_usd),
                    "current_price_usd": float(current_price),
                    "condition": alert.condition,
                    "triggered_at": alert.triggered_at.isoformat(),
                }
            )

            print(f"[Celery] 🔔 Notificação criada para {alert.user.email}: {alert.coin_name}")

    print("[Celery] Verificação de alertas concluída.")
