# game_catalog/urls.py
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('jogo/<int:jogo_id>/', views.jogo_detalhes, name='jogo_detalhes'),
    path('adicionar_jogo/', views.adicionar_jogo, name='adicionar_jogo'),
    path('editar_jogo/<int:jogo_id>', views.editar_jogo, name='editar_jogo'),
    path('avaliar_jogo/<int:jogo_id>/', views.avaliar_jogo, name='avaliar_jogo'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('api/jogos/', views.listar_jogos, name='listar_jogos'),
]
