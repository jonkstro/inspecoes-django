from django.urls import path
from . import views

urlpatterns = [
    path('', views.plano_manut, name='plano_manut'),
]