
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from plataforma.api.viewsets import PlanoManutViewset
from . import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'plano-manut', PlanoManutViewset, basename='PlanoManut')
urlpatterns = [
    path('', views.plano_manut, name='plano_manut'),
    path('', include(router.urls)),
]