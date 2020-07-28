import mapa.views as views
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('populate', views.populate, name='populate'),
]