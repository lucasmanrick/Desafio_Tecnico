from django.contrib import admin
from django.urls import path, include


from rest_framework import routers

from favorite.api import viewsets as favoriteviewsets
from portfolioholding.api import viewsets as portfolioholdingviewsets
from pricealert.api import viewsets as pricealertviewsets

route = routers.DefaultRouter()

route.register(r'favorites', favoriteviewsets.FavoriteViewSet, basename = 'Favorite')
route.register(r'portfolio', portfolioholdingviewsets.PortfolioHoldingViewSet, basename = 'Portfolio')
route.register(r'alerts', pricealertviewsets.PriceAlertViewSet, basename = 'Alerts')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),  #para todas rotas terem api/ na url.
    path('api/auth/', include('authentication.urls')),

]
