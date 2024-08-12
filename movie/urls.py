from django.urls import path
from .views import *


urlpatterns = [
    path('', movie, name='movie'),
    path('detail/<int:id>/', movie_detail, name='movie_detail'),
    path('search/', movie_search, name='movie_search'),
]