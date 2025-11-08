from django.contrib import admin
from django.urls import path, include


from rest_framework import routers

from favorite.api import viewsets as favoriteviewsets
from portfolioholding.api import viewsets as portfolioholdingviewsets
from pricealert.api import viewsets as pricealertviewsets
from notification.api import viewsets as notificationviewsets
from coinpricecache.views import CoinListView, CoinDetailView, CoinChartView
from notification.api.viewsets import  

route = routers.DefaultRouter()

route.register(r'favorites', favoriteviewsets.FavoriteViewSet, basename = 'Favorites')
route.register(r'portfolio', portfolioholdingviewsets.PortfolioHoldingViewSet, basename = 'Portfolio')
route.register(r'alerts', pricealertviewsets.PriceAlertViewSet, basename = 'Alerts')
route.register(r'notifications', notificationviewsets.NotificationViewSet, basename = 'Notifications')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),  #para todas rotas terem api/ na url.
    path('api/auth/', include('authentication.urls')),
    path('api/coins/', CoinListView.as_view()),  # GET /api/coins/
    path('api/coins/<str:coin_id>/', CoinDetailView.as_view()),      # GET /api/coins/<coin_id>/
    path('api/coins/<str:coin_id>/chart/', CoinChartView.as_view()),  # GET /api/coins/<coin_id>/chart/
    path('api/notifications/<str:coin_id>/read/', .as_view()),  # PATH /api/notifications/{id}/read/

]
