from django.contrib import admin
from django.urls import path, include


from rest_framework import routers

from favorite.api import viewsets as favoriteviewsets
from portfolioholding.api import viewsets as portfolioholdingviewsets
from pricealert.api import viewsets as pricealertviewsets
from notification.api import viewsets as notificationviewsets
from coinpricecache.api import viewsets as coinpricecacheviewsets

route = routers.DefaultRouter()

route.register(r'favorites', favoriteviewsets.FavoriteViewSet, basename = 'Favorites')
route.register(r'portfolio', portfolioholdingviewsets.PortfolioHoldingViewSet, basename = 'Portfolio')
route.register(r'alerts', pricealertviewsets.PriceAlertViewSet, basename = 'Alerts')
route.register(r'notifications', notificationviewsets.NotificationViewSet, basename = 'Notifications')
route.register(r'coins', coinpricecacheviewsets.CoinPriceCacheViewSet, basename = 'Coins')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),  #para todas rotas terem api/ na url.
    path('api/auth/', include('authentication.urls')),

]
