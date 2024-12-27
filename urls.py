from django.urls import path
from .views import get_currency

urlpatterns = [
    path('get-currency/', get_currency, name='get_currency'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('world/', include('world.urls')),
]