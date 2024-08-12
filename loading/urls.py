# loading/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('loading/', views.loading_page, name='loading_page'),
]
