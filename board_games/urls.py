"""Defnes URL patterns for board_games."""
from django.urls import path

from . import views

app_name = 'board_games'
upatterns = [
    #Home page
    path('', views.index, name ='index')
]