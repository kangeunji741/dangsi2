# loading/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('gest_login/', views.gest_login, name='gest_login'),
]
