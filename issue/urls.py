# loading/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue, name='issue'),
    path('detail/<int:id>/', views.issue_detail, name='issue_detail'),

]
