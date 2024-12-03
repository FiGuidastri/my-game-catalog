# game_catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.jogo_list, name='jogo_list'),
    path('jogo/<int:jogo_id>/', views.jogo_detalhes, name='jogo_detalhes'),
    path('adicionar_jogo/', views.adicionar_jogo, name='adicionar_jogo'),
]
