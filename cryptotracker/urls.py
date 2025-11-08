from django.contrib import admin
from django.urls import path, include


from rest_framework import routers

from favorite.api import viewsets as favoriteviewsets
from portfolioholding.api import viewsets as portfolioholdingviewsets
from pricealert.api import viewsets as pricealertviewsets
from notification.api import viewsets as notificationviewsets
from coinpricecache.views import CoinListView, CoinDetailView, CoinChartView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


route = routers.DefaultRouter()

route.register(r'favorites', favoriteviewsets.FavoriteViewSet, basename = 'Favorites')
route.register(r'portfolio', portfolioholdingviewsets.PortfolioHoldingViewSet, basename = 'Portfolio')
route.register(r'alerts', pricealertviewsets.PriceAlertViewSet, basename = 'Alerts')
route.register(r'notifications', notificationviewsets.NotificationViewSet, basename = 'Notifications')


urlpatterns = [
    # Necessário para o Swagger funcionar (mas não precisa expor no README)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),  #para todas rotas terem api/ na url.
    path('api/auth/', include('authentication.urls')),
    path('api/coins/', CoinListView.as_view()),  # GET /api/coins/
    path('api/coins/<str:coin_id>/', CoinDetailView.as_view()),      # GET /api/coins/<coin_id>/
    path('api/coins/<str:coin_id>/chart/', CoinChartView.as_view()),  # GET /api/coins/<coin_id>/chart/


]
